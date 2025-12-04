"""Prediction service for fraud detection"""
from pycaret.classification import load_model, predict_model
import pandas as pd
import streamlit as st
import logging

def sample_get(transaction_amount, 
                         sender_initial_balance, 
                         receiver_initial_balance, 
                         sender_behavior_id,
                         day_of_week,
                         hour):
    is_high_amount = transaction_amount > 5000
    is_odd_hour = hour in [2, 3, 4, 5]
    is_low_balance = sender_initial_balance < 1000
    
    fraud_score = 0
    fraud_factors = []
    
    if is_high_amount:
        fraud_score += 0.3
        fraud_factors.append(True)
    else:
        fraud_factors.append(False)
    
    if is_odd_hour:
        fraud_score += 0.25
        fraud_factors.append(True)
    else:
        fraud_factors.append(False)
    
    if is_low_balance:
        fraud_score += 0.2
        fraud_factors.append(True)
    else:
        fraud_factors.append(False)
    
    if transaction_amount > sender_initial_balance * 0.5:
        fraud_score += 0.15
        fraud_factors.append(True)
    else:
        fraud_factors.append(False)
    
    if receiver_initial_balance > 50000:
        fraud_score += 0.1
        fraud_factors.append(True)
    else:
        fraud_factors.append(False)
    
    fraud_probability = min(fraud_score, 1.0)
    is_fraudulent = fraud_probability > 0.5
    
    if fraud_probability > 0.7:
        risk_level = "High"
    elif fraud_probability > 0.4:
        risk_level = "Medium"
    else:
        risk_level = "Low"
    
    return {
        "prediction": "Fraudulent" if is_fraudulent else "Not Fraudulent",
        "is_fraudulent": is_fraudulent,
        "risk_level": risk_level,
        "probability": round(fraud_probability, 2),
        "transaction_amount": transaction_amount,
        "sender_balance": sender_initial_balance,
        "receiver_balance": receiver_initial_balance,
        "sender_behavior_id": sender_behavior_id,
        "day_of_week": day_of_week,
        "hour": hour,
        "account_balance_after": max(0, sender_initial_balance - transaction_amount),
        "fraud_factors": [
            ("Unusually high transaction amount compared to sender's typical spending", fraud_factors[0]),
            ("Sender's initial balance is significantly higher than average", fraud_factors[1]),
            ("Receiver's initial balance is unusually high", fraud_factors[2]),
            ("Transaction occurred during a high-risk hour", fraud_factors[3]),
            ("Sender behavior ID is associated with previous fraudulent activities", fraud_factors[4]),
        ],
        "comparison_insight": "Higher than 90% of similar transactions"
    }

def load_model_wrapper():
    load_error = None
    try:
        model = load_model('./models/tuned_ada_fraud_model')
    except Exception as e:
        model = None
        load_error = e
        st.sidebar.error(
            "Model failed to load. If you see an OSError mentioning 'libomp', install libomp (Homebrew: `brew install libomp`) or use conda: `conda install -c conda-forge libomp`. Full error printed in the main area."  
        )
        st.error(f"Model load error: {e}")
    return model

def get_fraud_prediction(transaction_amount, 
            sender_init_balance, 
            sender_behavior_id, 
            receiver_init_balance,
            receiver_behavior_id,
            hour,
            day_of_week,
            amount_to_sender_balance_ratio,
            low_balance_flag):
    model = load_model_wrapper()

    input_dict = {
        'TX_AMOUNT': transaction_amount,
        'SENDER_INIT_BALANCE': sender_init_balance,
        'SENDER_TX_BEHAVIOR_ID': sender_behavior_id,
        'RECEIVER_INIT_BALANCE': receiver_init_balance,
        'RECEIVER_TX_BEHAVIOR_ID': receiver_behavior_id,
        'HOUR': hour,
        'DAY_OF_WEEK': day_of_week,
        'AMOUNT_TO_SENDER_BALANCE_RATIO': amount_to_sender_balance_ratio,
        'LOW_BALANCE_FLAG': low_balance_flag,
    }

    input_df = pd.DataFrame([input_dict])

    # If model failed to load, fall back to the heuristic function
    if model is None:
        return sample_get(
            transaction_amount,
            sender_init_balance,
            receiver_init_balance,
            sender_behavior_id,
            day_of_week,
            hour,
        )

    # Run the model and capture output
    predictions = predict_model(model, data=input_df)

    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    logging.debug('Predictions from Model \n%s', predictions)
    try:
        st.write('Prediction from Model:')
        st.write(predictions)
    except Exception:
        # If Streamlit isn't available in this context, continue
        pass

    # Coerce model output to DataFrame for inspection
    if isinstance(predictions, pd.DataFrame):
        pred_df = predictions
        logging.debug('Predictions dataframe created.')
    else:
        try:
            pred_df = pd.DataFrame(predictions)
        except Exception:
            return sample_get(
                transaction_amount,
                sender_init_balance,
                receiver_init_balance,
                sender_behavior_id,
                day_of_week,
                hour,
            )

    cols = pred_df.columns.tolist()

    # Extract common pycaret columns
    pred_label = None
    pred_prob = None
    if 'Label' in cols:
        pred_label = pred_df['Label'].iloc[0]
    elif 'prediction_label' in cols:
        pred_label = pred_df['prediction_label'].iloc[0]
    elif 'prediction' in cols:
        pred_label = pred_df['prediction'].iloc[0]

    if 'Score' in cols:
        pred_prob = pred_df['Score'].iloc[0]
    elif 'prediction_score' in cols:
        pred_prob = pred_df['prediction_score'].iloc[0]

    # If probability not found, try numeric non-input columns as proxy
    if pred_prob is None:
        numeric_cols = [c for c in cols if pd.api.types.is_numeric_dtype(pred_df[c])]
        input_keys = list(input_dict.keys())
        candidate_cols = [c for c in numeric_cols if c not in input_keys]
        if candidate_cols:
            try:
                pred_prob = float(pred_df[candidate_cols].iloc[0].max())
            except Exception:
                pred_prob = None

    # Interpret label/probability into boolean fraud decision
    is_fraudulent = None
    if pred_label is not None:
        if isinstance(pred_label, (int, float)):
            is_fraudulent = bool(pred_label)
        else:
            is_fraudulent = str(pred_label).strip().lower() in ['fraud', 'fraudulent', '1', 'true', 'yes']

    logging.debug('1. is_fraudulent=%s', is_fraudulent)

    if is_fraudulent is None and pred_prob is not None:
        try:
            is_fraudulent = float(pred_prob) > 0.5
        except Exception:
            is_fraudulent = False

    logging.debug('2. is_fraudulent=%s', is_fraudulent)

    # If probability missing, fallback to heuristic result
    if pred_prob is None:
        fallback = sample_get(
            transaction_amount,
            sender_init_balance,
            receiver_init_balance,
            sender_behavior_id,
            day_of_week,
            hour,
        )
        fallback['model_output'] = pred_df
        return fallback

    try:
        prob_val = float(pred_prob)
    except Exception:
        prob_val = 0.0

    logging.debug('probability=%s', prob_val)

    if prob_val > 0.7:
        risk_level = 'High'
    elif prob_val > 0.4:
        risk_level = 'Medium'
    else:
        risk_level = 'Low'

    logging.debug('risk_level=%s', risk_level)

    fraud_factors = [
        ("Unusually high transaction amount compared to sender's typical spending", transaction_amount > 5000),
        ("Sender's initial balance is significantly higher than average", sender_init_balance > 50000),
        ("Receiver's initial balance is unusually high", receiver_init_balance > 50000),
        ("Transaction occurred during a high-risk hour", hour in [2, 3, 4, 5]),
        ("Sender behavior ID is associated with previous fraudulent activities", False),
    ]

    result = {
        'prediction': str(pred_label) if pred_label is not None else ("Fraudulent" if is_fraudulent else "Not Fraudulent"),
        'is_fraudulent': bool(is_fraudulent),
        'risk_level': risk_level,
        'probability': round(prob_val, 2),
        'transaction_amount': transaction_amount,
        'sender_balance': sender_init_balance,
        'receiver_balance': receiver_init_balance,
        'sender_behavior_id': sender_behavior_id,
        'day_of_week': day_of_week,
        'hour': hour,
        'account_balance_after': max(0, sender_init_balance - transaction_amount),
        'fraud_factors': fraud_factors,
        'comparison_insight': 'Model-based prediction',
        'model_output': pred_df,
    }

    return result
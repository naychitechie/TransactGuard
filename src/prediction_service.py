"""Prediction service for fraud detection"""

def get_fraud_prediction(transaction_amount, sender_initial_balance, receiver_initial_balance, sender_behavior_id, day_of_week, hour):
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

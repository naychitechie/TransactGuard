# TransactGuard - Fraud Transaction Prediction Tool

Fraud detection web app built with Streamlit, deployed on Azure Web App.

# Problem Definition

Financial institutions process millions of transactions daily, and detecting fraudulent activity in real time is critical to protect customers and maintain trust. Traditional rule-based systems are rigid, generate high false positives, and fail to adapt to evolving fraud patterns. This project aims to build a predictive model that classifies transactions as fraudulent or legitimate using structured transaction data, enabling faster, more accurate, and scalable fraud detection. 

# Business Goals
1.	Build a Baseline Fraud Prediction Model – Train and evaluate a supervised learning model to classify transactions as fraudulent or legitimate using historical structured transaction data. 
2.	Optimize Model Performance – Experiment with different algorithms and improve accuracy, precision, and recall balancing fraud detection and false positives. 
3.	Generate Actionable Insights – Identify which transaction features (e.g., amount, frequency, location) contribute most to fraud detection to support interpretability and learning. 
4.	Simulate Real-World Application – Demonstrate the model’s potential use in a financial setting by testing it on unseen data and evaluating practical trade-offs (e.g., detection rate vs. false alarms). 

## Tech Stack

- **Language:** Python 3.10
- **Framework:** Streamlit
- **Cloud Platform:** Azure Web App
- **CI/CD:** GitHub Actions

## Project Structure

- **.github/workflows/**: Contains the CI/CD pipeline configuration (`main_transactguard.yml`) for automating builds and deployments to Azure.
- **data/**: Stores datasets used for training and testing the fraud detection model.
- **models/**: Contains serialized machine learning models (e.g., `.pkl` files) used for inference.
- **pages/**: Holds additional Streamlit pages for the multi-page application structure.
- **src/**: Source code directory containing utility scripts and model definitions.
- **app.py**: The main entry point for the Streamlit application, handling the UI and interaction logic.
- **requirements.txt**: Defines the Python dependencies required to run the application.
- **README.md**: Project documentation, including setup steps and feature overview.

## Setup and Installation

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## Features

- Dark theme UI matching mockups
- Right-aligned sidebar navigation
- Mock prediction engine (Phase 4-ready)
- Interactive data explorer with Plotly
- Session state management

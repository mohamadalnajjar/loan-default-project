import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Loan Default Predictor",
    page_icon="💳",
    layout="centered"
)

# Load trained model
model = joblib.load("models/random_forest_model.pkl")

st.sidebar.title("About")

st.sidebar.info(
    """
    This application uses a Random Forest machine learning model
    trained on the Give Me Some Credit dataset to estimate
    loan default risk.

    The model predicts:
    - probability of default
    - predicted default class
    - borrower risk band

    Developed as part of an Engineering Project: Classification.
    """
)

st.title("Loan Default Prediction App")

st.write(
    "This app predicts whether a borrower is likely to default on a loan "
    "based on financial and demographic information."
)

st.warning(
    "This tool is for educational decision-support only and should not be used as the sole basis for real financial decisions."
)

st.header("Borrower Information")

revolving_utilization = st.number_input(
    "Revolving Utilization of Unsecured Lines",
    min_value=0.0,
    value=0.2
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=120,
    value=35
)

past_due_30_59 = st.number_input(
    "Number of Times 30-59 Days Past Due",
    min_value=0,
    value=0
)

debt_ratio = st.number_input(
    "Debt Ratio",
    min_value=0.0,
    value=0.3
)

monthly_income = st.number_input(
    "Monthly Income",
    min_value=0.0,
    value=5000.0
)

open_credit_lines = st.number_input(
    "Number of Open Credit Lines and Loans",
    min_value=0,
    value=5
)

times_90_late = st.number_input(
    "Number of Times 90 Days Late",
    min_value=0,
    value=0
)

real_estate_loans = st.number_input(
    "Number of Real Estate Loans or Lines",
    min_value=0,
    value=1
)

past_due_60_89 = st.number_input(
    "Number of Times 60-89 Days Past Due",
    min_value=0,
    value=0
)

dependents = st.number_input(
    "Number of Dependents",
    min_value=0,
    value=0
)

if st.button("Predict Default Risk"):
    input_data = pd.DataFrame({
        "RevolvingUtilizationOfUnsecuredLines": [revolving_utilization],
        "age": [age],
        "NumberOfTime30-59DaysPastDueNotWorse": [past_due_30_59],
        "DebtRatio": [debt_ratio],
        "MonthlyIncome": [monthly_income],
        "NumberOfOpenCreditLinesAndLoans": [open_credit_lines],
        "NumberOfTimes90DaysLate": [times_90_late],
        "NumberRealEstateLoansOrLines": [real_estate_loans],
        "NumberOfTime60-89DaysPastDueNotWorse": [past_due_60_89],
        "NumberOfDependents": [dependents]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if probability < 0.2:
        risk_band = "Low Risk"
        decision = "Likely eligible for a loan"
        decision_type = "success"
    elif probability < 0.5:
        risk_band = "Medium Risk"
        decision = "May be eligible, but requires manual review"
        decision_type = "warning"
    else:
        risk_band = "High Risk"
        decision = "Not recommended for loan approval"
        decision_type = "error"

    st.subheader("Prediction Result")

    st.write(f"**Predicted Default:** {'Yes' if prediction == 1 else 'No'}")
    st.write(f"**Default Probability:** {probability:.2%}")

    if risk_band == "Low Risk":
        st.success(f"Risk Band: {risk_band}")
    elif risk_band == "Medium Risk":
        st.warning(f"Risk Band: {risk_band}")
    else:
        st.error(f"Risk Band: {risk_band}")

    st.subheader("Loan Eligibility Decision")

    if decision_type == "success":
        st.success(decision)
    elif decision_type == "warning":
        st.warning(decision)
    else:
        st.error(decision)

    st.caption(
        "This decision is based on the model's estimated default risk and should be reviewed by a financial officer before final approval."
    )
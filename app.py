import streamlit as st
import pandas as pd
import joblib

# 1. Load the saved pipeline
model = joblib.load('churn_model.pkl')

# 2. Set up the UI
st.set_page_config(page_title="Bank Churn Predictor", layout="centered")
st.title("🏦 Bank Customer Churn Predictor")

# 3. Create Input Fields
st.header("Customer Profile")
col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", 300, 850, 650)
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.slider("Age", 18, 100, 38)
    tenure = st.slider("Tenure (Years)", 0, 10, 5)

with col2:
    balance = st.number_input("Account Balance ($)", 0.0, 300000.0, 50000.0)
    num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
    has_card = st.radio("Has Credit Card?", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    is_active = st.radio("Is Active Member?", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    salary = st.number_input("Estimated Annual Salary ($)", 0.0, 200000.0, 100000.0)

# 4. Prediction Logic
input_df = pd.DataFrame({
    'CreditScore': [credit_score], 'Geography': [geography], 'Gender': [gender],
    'Age': [age], 'Tenure': [tenure], 'Balance': [balance],
    'NumOfProducts': [num_products], 'HasCrCard': [has_card],
    'IsActiveMember': [is_active], 'EstimatedSalary': [salary]
})

if st.button("Calculate Churn Risk"):
    prediction = model.predict(input_df)
    # Get probability of the predicted class
    prob = model.predict_proba(input_df)[0]
    
    # In your LabelEncoder, 0 is Churned and 1 is Retained
    if prediction[0] == 0:
        st.error("Verdict: **Churn Risk Detected**")
        st.write(f"Confidence: {prob[0]:.1%}")
    else:
        st.success("Verdict: **Customer Likely to Stay**")
        st.write(f"Confidence: {prob[1]:.1%}")
import streamlit as st
import requests

API_URL="http://127.0.0.1:8000/predict"

st.write("App started successfully")

st.title("Insurance Predictor")

st.markdown("Enter your details below:")

#Input Fields
age = st.number_input("Age",min_value=1,max_value=120,value=30)
height = st.number_input("Height",min_value=1.0,max_value=2.0,value=1.85)
weight = st.number_input("Weight",min_value=1.0,max_value=200.0,value=101.4)
income_lpa = st.number_input("Income LPA",min_value=0.0,max_value=100.0,value=28.95)
smoker = st.selectbox("Are you a smoker?",options=["Yes","No"])
city = st.text_input("Your City")
occupation = st.selectbox("your Occupation",options=['retired', 'freelancer', 'student', 'government_job',
    'business_owner', 'unemployed', 'private_job'])

if st.button("Predict"):
    input_data = {
        "age" : age,
        "height" : height,
        "weight" : weight,
        "income_lpa" : income_lpa,
        "smoker" : smoker,
        "city" : city,
        "occupation" : occupation
    }
    try:
        response = requests.post(API_URL,json=input_data)
        st.write("Status Code:", response.status_code)

        if response.status_code == 200:
            result =response.json()
            st.success(f"Predicted Category: **{result['predicted_category']}**")
        else:
            st.error(f"API ERROR: {response.status_code} - { response.text}")
    except Exception as e:
        st.error(f"Connection failed: {e}")



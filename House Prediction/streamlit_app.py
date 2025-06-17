import streamlit as st
import pandas as pd
import pickle

# Load model
with open('House_Prediction_Model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("House Price Prediction")

# User inputs (adjust features as per your dataset)
total_sqft = st.number_input("Total Square Feet", min_value=100, max_value=10000, value=1000)
bhk = st.number_input("BHK", min_value=1, max_value=10, value=3)
bath = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

# Create input DataFrame
input_data = pd.DataFrame({
    'total_sqft': [total_sqft],
    'bhk': [bhk],
    'bath': [bath]
})

# Predict on button click
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Predicted House Price: Rs {round(prediction[0], 2)} Lakhs")

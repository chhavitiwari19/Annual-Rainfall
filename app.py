import streamlit as st
import joblib
import numpy as np

st.title("🌧️Annual Rainfall Prediction")
st.write("Predict annual rainfall using seasonal rainfall data.")

# Load the trained model
try:
    model = joblib.load("Predicted Annual Rainfall.pkl")
except Exception as e:
    st.error(f"Could not load model: {e}")
    st.stop()

# Input features
st.subheader("Enter Seasonal Rainfall Details")

jan_feb = st.number_input("January-February Rainfall (mm)", min_value=0.0, value=50.0)
mar_may = st.number_input("March-May Rainfall (mm)", min_value=0.0, value=100.0)
jun_sep = st.number_input("June-September Rainfall (mm)", min_value=0.0, value=500.0)
oct_dec = st.number_input("October-December Rainfall (mm)", min_value=0.0, value=100.0)

if st.button("Predict Annual Rainfall"):
    input_data = np.array([[
        jan_feb,
        mar_may,
        jun_sep,
        oct_dec
    ]])

    prediction = model.predict(input_data)
    st.success(f"Predicted Annual Rainfall: {prediction[0]:.2f} mm")


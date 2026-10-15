import streamlit as st
import joblib
import numpy as np

# App title
st.title("🌧️ Annual Rainfall Prediction")
st.write("Predict annual rainfall using Machine Learning.")

# Load the trained model
try:
    model = joblib.load("Predicted Annual Rainfall.pkl")
    st.success("Rainfall model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# User inputs
st.subheader("Enter Weather Details")

day = st.number_input("Day", min_value=1, max_value=31, value=15)
pressure = st.number_input("Pressure", value=1010.0)
maxtemp = st.number_input("Maximum Temperature", value=30.0)
humidity = st.number_input(
    "Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

# Predict rainfall
if st.button("Predict Rainfall"):
    input_data = np.array([[day, pressure, maxtemp, humidity]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Annual Rainfall: {prediction[0]:.2f}")

# Predict rainfall
if st.button("Predict Rainfall"):
    input_data = np.array([[temperature, humidity]])

    try:
        prediction = model.predict(input_data)
        st.success(
            f"Predicted Annual Rainfall: {prediction[0]:.2f}"
        )
    except Exception as e:
        st.error(f"Prediction error: {e}")

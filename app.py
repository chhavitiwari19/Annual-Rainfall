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

temperature = st.number_input(
    "Average Temperature",
    min_value=0.0,
    max_value=60.0,
    value=25.0
)

humidity = st.number_input(
    "Average Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

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

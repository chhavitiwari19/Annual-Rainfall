import streamlit as st
import pickle
import numpy as np

# Load the trained rainfall prediction model
with open("Predicted Annual Rainfall.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("🌧️ Annual Rainfall Prediction")
st.write("Predict annual rainfall using Machine Learning.")

# User input
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

# Prediction button
if st.button("Predict Rainfall"):

    # Prepare input for the model
    input_data = np.array([[temperature, humidity]])

    # Predict
    prediction = model.predict(input_data)

    # Display result
    st.success(
        f"Predicted Annual Rainfall: {prediction[0]:.2f}"
    )

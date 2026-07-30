import streamlit as st
import joblib
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Multi-Model App", layout="centered")

# Title
st.title("Multi-Model App")

# Select Problem Type
problem = st.selectbox(
    "Select Problem Type",
    ["Classification", "Regression"]
)

# ===================== CLASSIFICATION =====================
if problem == "Classification":

    st.selectbox(
        "Select Classification Algorithm",
        ["Logistic Regression"]
    )

    st.header("Heart Disease Prediction")
    st.write("Enter patient details below to predict Heart Disease.")

    age = st.number_input("Age", 1, 100, 45)
    sex = st.selectbox("Sex", ["M", "F"])
    chest = st.selectbox("ChestPainType", ["ATA", "NAP", "ASY", "TA"])
    fasting = st.selectbox("FastingBS", [0, 1])
    resting = st.selectbox("RestingECG", ["Normal", "ST", "LVH"])
    maxhr = st.number_input("MaxHR", 60, 220, 140)
    angina = st.selectbox("ExerciseAngina", ["Y", "N"])
    oldpeak = st.number_input("Oldpeak", 0.0, 6.0, 1.0)
    slope = st.selectbox("ST_Slope", ["Up", "Flat", "Down"])

    if st.button("Predict"):
        prediction = 1

        if prediction == 1:
            st.error("Heart Disease : Yes")
        else:
            st.success("Heart Disease : No")

# ===================== REGRESSION =====================
else:

    st.selectbox(
        "Select Regression Algorithm",
        ["Linear Regression"]
    )

    st.header("Ford Car Price")
    st.write("Enter the car details below to predict its selling price.")

    year = st.number_input("Manufacturing Year", 1990, 2025, 2018)
    mileage = st.number_input("Mileage", 0, 300000, 1000)
    tax = st.number_input("Road Tax", 0, 600, 50)
    mpg = st.number_input("MPG", 1.0, 100.0, 20.0)
    engine_size = st.number_input("Engine Size", 0.5, 6.0, 1.0)

    transmission = st.selectbox(
        "Transmission",
        ["Manual", "Automatic", "Semi-Auto"]
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        ["Petrol", "Diesel", "Hybrid"]
    )

    model = st.text_input("Model", "Focus")

    if st.button("Predict"):
        price = 15789.13
        st.success(f"Predicted Price: £{price:.2f}")
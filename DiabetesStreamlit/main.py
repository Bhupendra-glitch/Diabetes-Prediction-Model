
import streamlit as st
import pickle
import numpy as np

# Load your trained model (make sure you have saved it as 'diabetes_model.pkl')
# model = pickle.load(open("diabetes_model.pkl", "rb"))

st.title("🩺 Diabetes Prediction App")
st.write("Enter patient details to predict the likelihood of having diabetes.")

# Input fields
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, format="%.1f")
insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=80)
age = st.number_input("Age", min_value=1, max_value=120, value=30)
bp = st.number_input("Blood Pressure", min_value=0, max_value=200, value=80)
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, format="%.2f")

# Convert input to numpy array
features = np.array([[pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error("⚠️ The patient is likely to have diabetes.")
    else:
        st.success("✅ The patient is not likely to have diabetes.")


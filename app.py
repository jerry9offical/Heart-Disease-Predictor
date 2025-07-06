
import streamlit as st
import pandas as pd
import joblib
from PIL import Image

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")
st.title("❤️ Heart Disease Predictor")
st.markdown("Predict the presence of heart disease based on patient details.")

try:
    image = Image.open("Heart 2.jpg")
    st.image(image, caption="Heart Disease Illustration", use_column_width=True)
except Exception as e:
    st.warning(f"Could not load image: {e}")

st.write("---")

model = joblib.load("heart_model.joblib")

st.subheader("🧾 Enter Patient Details")

cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
thalach = st.number_input("Max Heart Rate Achieved (thalach)", 60, 220)
slope = st.selectbox("Slope of ST Segment (slope)", [0, 1, 2])
restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])
fbs = st.selectbox("Fasting Blood Sugar > 120mg/dl (fbs)", [0, 1])
sex = st.selectbox("Sex (1 = Male, 0 = Female)", [0, 1])
thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])
ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3])
exang = st.selectbox("Exercise-Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 6.5)

if st.button("Predict"):
    input_data = pd.DataFrame([[cp, thalach, slope, restecg, fbs, sex, thal, ca, exang, oldpeak]],
                              columns=["cp", "thalach", "slope", "restecg", "fbs", "sex", "thal", "ca", "exang", "oldpeak"])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ The model predicts the presence of heart disease.")
    else:
        st.success("✅ The model predicts no heart disease.")

# Heart Disease Predictor

A machine learning project that predicts the presence of heart disease using logistic regression, based on patient health metrics.

---

## 💻 Project Overview

This project uses the UCI Heart Disease dataset and applies logistic regression to predict whether a person has heart disease based on attributes like chest pain type, maximum heart rate, exercise-induced angina, and more.

---

## 📁 Dataset

- Source: [UCI Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
- File: `heart.csv`
- Total Records: 1025
- Target Variable: `target` (1 = disease, 0 = no disease)

---

## 🧪 Features Used

| Feature     | Description                                  |
|-------------|----------------------------------------------|
| `cp`        | Chest pain type                              |
| `thalach`   | Max heart rate achieved                      |
| `slope`     | Slope of the peak exercise ST segment        |
| `restecg`   | Resting electrocardiographic results         |
| `fbs`       | Fasting blood sugar > 120 mg/dl (1 = true)   |
| `sex`       | Gender (1 = male, 0 = female)                |
| `thal`      | Thalassemia                                  |
| `ca`        | Number of major vessels (0-3) colored        |
| `exang`     | Exercise-induced angina (1 = yes, 0 = no)    |
| `oldpeak`   | ST depression induced by exercise            |

---

## 🔧 Tech Stack

- Python
- Pandas
- Seaborn & Matplotlib (EDA)
- Scikit-learn (modeling & evaluation)
- Joblib (model saving)

---

## 🧠 Model

- **Algorithm**: Logistic Regression
- **Accuracy**: ~82.4%
- **Evaluation**: Precision, Recall, F1-score using classification report

---

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/heart_disease_predictor.git
   cd heart_disease_predictor

2. Install dependencies:
   pip install -r requirements.txt

3. Run the script:
   python model.py

   # 🫀 Heart Disease Predictor App

[![Streamlit App](https://img.shields.io/badge/View%20App-Streamlit-blue?logo=streamlit)](https://heart-disease-predictor-cwqsbnxzpwywvsf6bxdbjz.streamlit.app/)

A machine learning-powered Streamlit app that predicts the likelihood of heart disease using key clinical features.

---

## 🚀 Live Demo

🔗 [Click here to open the app](https://heart-disease-predictor-cwqsbnxzpwywvsf6bxdbjz.streamlit.app/)

---

## 🧠 Overview

This app uses a **logistic regression model** trained on heart disease patient data to provide real-time predictions based on:

- Chest pain type (cp)
- Max heart rate (thalach)
- Slope of ST segment (slope)
- Resting ECG (restecg)
- Fasting blood sugar (fbs)
- Sex
- Thalassemia (thal)
- Number of major vessels (ca)
- Exercise-induced angina (exang)
- ST depression (oldpeak)

---

## 🎯 Features

- ✅ Clean UI with **dark mode**
- ✅ Real-time predictions using a trained **logistic regression** model
- ✅ Custom patient input form
- ✅ Medical illustration for visual context
- ✅ Deployed on **Streamlit Cloud**

---

## 📁 Project Structure







   

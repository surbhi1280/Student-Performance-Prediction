import streamlit as st
import joblib
import pandas as pd
import numpy as np

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Student Performance Prediction App")
st.write("Predict a student's exam score using academic and socio-economic factors.")

# -------------------------------
# Load Model and Columns
# -------------------------------
model = joblib.load("best_student_model.pkl")
cols = joblib.load("columns.pkl")

# -------------------------------
# User Inputs
# -------------------------------

Hours_Studied = st.number_input("Hours Studied", 0.0, 24.0, 5.0)
Attendance = st.number_input("Attendance (%)", 0.0, 100.0, 75.0)
Sleep_Hours = st.number_input("Sleep Hours", 0.0, 12.0, 7.0)
Previous_Scores = st.number_input("Previous Scores", 0.0, 100.0, 70.0)
Tutoring_Sessions = st.number_input("Tutoring Sessions per Week", 0.0, 10.0, 1.0)
Physical_Activity = st.number_input("Physical Activity (hrs/week)", 0.0, 20.0, 3.0)

Parental_Involvement = st.selectbox("Parental Involvement", [0,1,2])
Access_to_Resources = st.selectbox("Access to Resources", [0,1,2])
Extracurricular_Activities = st.selectbox("Extracurricular Activities", [0,1])
Motivation_Level = st.selectbox("Motivation Level", [0,1,2])
Internet_Access = st.selectbox("Internet Access", [0,1])
Family_Income = st.selectbox("Family Income", [0,1,2])
Teacher_Quality = st.selectbox("Teacher Quality", [0,1,2])
School_Type = st.selectbox("School Type", [0,1])
Peer_Influence = st.selectbox("Peer Influence", [0,1,2])
Learning_Disabilities = st.selectbox("Learning Disabilities", [0,1])
Parental_Education_Level = st.selectbox("Parental Education Level", [0,1,2])
Distance_from_Home = st.selectbox("Distance from Home", [0,1,2])
Gender = st.selectbox("Gender", [0,1])

# -------------------------------
# Prediction
# -------------------------------

if st.button("Predict Score"):

    input_data = {
        "Hours_Studied": Hours_Studied,
        "Attendance": Attendance,
        "Parental_Involvement": Parental_Involvement,
        "Access_to_Resources": Access_to_Resources,
        "Extracurricular_Activities": Extracurricular_Activities,
        "Sleep_Hours": Sleep_Hours,
        "Previous_Scores": Previous_Scores,
        "Motivation_Level": Motivation_Level,
        "Internet_Access": Internet_Access,
        "Tutoring_Sessions": Tutoring_Sessions,
        "Family_Income": Family_Income,
        "Teacher_Quality": Teacher_Quality,
        "School_Type": School_Type,
        "Peer_Influence": Peer_Influence,
        "Physical_Activity": Physical_Activity,
        "Learning_Disabilities": Learning_Disabilities,
        "Parental_Education_Level": Parental_Education_Level,
        "Distance_from_Home": Distance_from_Home,
        "Gender": Gender
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # 🔥 VERY IMPORTANT — match training column order
    input_df = input_df[model.feature_names_in_]

    prediction = model.predict(input_df)[0]
    prediction = np.clip(prediction, 0, 100)

    st.success(f"🎯 Predicted Exam Score: {round(prediction, 2)}")


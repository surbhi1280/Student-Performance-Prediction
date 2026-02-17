from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# 🔹 Load FULL trained pipeline model only
model = joblib.load("best_student_model.pkl")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    # Collect all form values
    input_data = {
        "Hours_Studied": float(request.form['Hours_Studied']),
        "Attendance": float(request.form['Attendance']),
        "Parental_Involvement": int(request.form['Parental_Involvement']),
        "Access_to_Resources": int(request.form['Access_to_Resources']),
        "Extracurricular_Activities": int(request.form['Extracurricular_Activities']),
        "Sleep_Hours": float(request.form['Sleep_Hours']),
        "Previous_Scores": float(request.form['Previous_Scores']),
        "Motivation_Level": int(request.form['Motivation_Level']),
        "Internet_Access": int(request.form['Internet_Access']),
        "Tutoring_Sessions": float(request.form['Tutoring_Sessions']),
        "Family_Income": int(request.form['Family_Income']),
        "Teacher_Quality": int(request.form['Teacher_Quality']),
        "School_Type": int(request.form['School_Type']),
        "Peer_Influence": int(request.form['Peer_Influence']),
        "Physical_Activity": float(request.form['Physical_Activity']),
        "Learning_Disabilities": int(request.form['Learning_Disabilities']),
        "Parental_Education_Level": int(request.form['Parental_Education_Level']),
        "Distance_from_Home": int(request.form['Distance_from_Home']),
        "Gender": int(request.form['Gender'])
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Predict
    prediction = model.predict(input_df)[0]

    # Clip score between 0–100
    prediction = np.clip(prediction, 0, 100)

    return render_template(
        'index.html',
        prediction_text=f"Predicted Exam Score: {round(prediction, 2)}"
    )


if __name__ == "__main__":
    app.run(debug=True)

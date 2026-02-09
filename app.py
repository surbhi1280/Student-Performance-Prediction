from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained ML model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form values safely
        study_hours = float(request.form.get("study_hours", 0))
        attendance = float(request.form.get("attendance", 0))
        grades = float(request.form.get("grades", 0))
        activities = request.form.get("activities")
        education = request.form.get("education")

        # Validation
        if study_hours <= 0 or attendance <= 0 or grades <= 0:
            return render_template(
                "index.html",
                prediction="Please enter valid numeric values"
            )

        # Prepare input data
        data = {
            "study_hours_per_week": [study_hours],
            "attendance_rate": [attendance],
            "previous_grades": [grades],
            "participation_in_extracurricular_activities": [activities],
            "parent_education_level": [education]
        }

        df = pd.DataFrame(data)

        # One-hot encoding
        df = pd.get_dummies(df)

        # Align columns with training model
        df = df.reindex(columns=model.feature_names_in_, fill_value=0)

        # Prediction
        prediction = model.predict(df)
        result = "PASS" if prediction[0] == 1 else "FAIL"

        return render_template("index.html", prediction=result)

    except Exception:
        return render_template(
            "index.html",
            prediction="Error! Please fill all fields correctly."
        )

if __name__ == "__main__":
    app.run(debug=True)

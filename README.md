🎓 Student Performance Prediction
📌 Project Overview

-This is a Machine Learning web application that predicts a student's Exam Score based on academic and socio-economic factors.
-The model is trained using multiple regression algorithms and deployed using Flask.

🚀 Features

-Predicts student exam performance
-Uses academic + personal + socio-economic factors
-Trained on multiple ML models
-Best model selected using R² score
-Clean web interface using Flask
-Score range clipped between 0–100
-Ready for deployment

📊 Input Features

The model uses the following features:
-Hours_Studied
-Attendance
-Parental_Involvement
-Access_to_Resources
-Extracurricular_Activities
-Sleep_Hours
-Previous_Scores
-Motivation_Level
-Internet_Access
-Tutoring_Sessions
-Family_Income
-Teacher_Quality
-School_Type
-Peer_Influence
-Physical_Activity
-Learning_Disabilities
-Parental_Education_Level
-Distance_from_Home

Gender

🧠 Machine Learning Models Used
-Linear Regression
-Ridge Regression
-Lasso Regression
-Decision Tree Regressor
-Random Forest Regressor
-SVR
-KNN
Best model selected based on R² score performance.

🛠️ Tech Stack
-Python
-Pandas
-NumPy
-Scikit-learn
-Flask
-HTML / CSS

📂 Project Structure
Student-Performance-Prediction/
│
├── app.py
├── best_student_model.pkl
├── columns.pkl
├── templates/
│   └── index.html
├── requirements.txt
└── README.md

📈 Model Evaluation

Model performance evaluated using:
-R² Score
-Mean Squared Error (MSE)
-Root Mean Squared Error (RMSE)

import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load 500-student dataset
data = pd.read_excel("student_data_500.xlsx")

X = data[[
    "ATTENDENCE",
    "STUDY HOURS",
    "PREVIOUS MARKS",
    "ASSIGNMENT COMPLETION"
]]

y = data["FINAL MARKS"]

model = RandomForestRegressor(n_estimators=100)

model.fit(X, y)

attendance = 85
study_hours = 4
previous_marks = 80
assignment = 90

prediction = model.predict([[
    attendance,
    study_hours,
    previous_marks,
    assignment
]])

print("Predicted Marks:", round(prediction[0], 2))

import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_excel("student_data_500.xlsx")

X = data[[
    "ATTENDENCE",
    "STUDY HOURS",
    "PREVIOUS MARKS",
    "ASSIGNMENT COMPLETION"
]]

y = data["FINAL MARKS"]

# Train AI
model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

st.title("🎓 AI Student Performance Predictor")

attendance = st.slider("Attendance (%)", 0, 100, 85)
study_hours = st.slider("Study Hours Per Day", 0, 10, 4)
previous_marks = st.slider("Previous Marks", 0, 100, 80)
assignment = st.slider("Assignment Completion (%)", 0, 100, 90)

st.subheader("📊 Student Dataset Analytics")

col1, col2 = st.columns(2)

with col1:
    fig1 = px.histogram(
        data,
        x="FINAL MARKS",
        title="Distribution of Final Marks"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.scatter(
        data,
        x="ATTENDENCE",
        y="FINAL MARKS",
        title="Attendance vs Final Marks"
    )
    st.plotly_chart(fig2, use_container_width=True)

if st.button("Predict"):

    prediction = model.predict([[
        attendance,
        study_hours,
        previous_marks,
        assignment
    ]])

    marks = round(prediction[0], 2)

    st.success(f"Predicted Marks: {marks}")

    st.subheader("📈 Student Comparison")

    comparison = pd.DataFrame({
        "Metric": [
            "Attendance",
            "Study Hours",
            "Previous Marks",
            "Assignment Completion",
            "Predicted Marks"
        ],
        "Value": [
            attendance,
            study_hours,
            previous_marks,
            assignment,
            marks
        ]
    })

    st.bar_chart(comparison.set_index("Metric"))

    if marks >= 85:
        st.write("Performance: Excellent 🏆")
        st.success("Risk Level: Low")
        st.balloons()

    elif marks >= 70:
        st.write("Performance: Good 👍")
        st.info("Risk Level: Medium")

    elif marks >= 50:
        st.write("Performance: Average 📚")
        st.warning("Risk Level: Medium")

    else:
        st.write("Performance: At Risk ⚠️")
        st.error("Risk Level: High")

    st.subheader("AI Recommendations")

    if attendance < 75:
        st.write("✅ Improve attendance")

    if study_hours < 3:
        st.write("✅ Increase study hours")

    if previous_marks < 60:
        st.write("✅ Focus on weak subjects")

    if assignment < 80:
        st.write("✅ Complete assignments regularly")
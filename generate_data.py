import pandas as pd
import random

data = []

for i in range(500):
    attendance = random.randint(40, 100)
    study_hours = random.randint(1, 8)
    previous_marks = random.randint(35, 100)
    assignment = random.randint(40, 100)

    final_marks = (
        attendance * 0.2
        + study_hours * 5
        + previous_marks * 0.5
        + assignment * 0.2
    )

    final_marks += random.randint(-5, 5)

    final_marks = max(35, min(100, round(final_marks)))

    data.append([
        attendance,
        study_hours,
        previous_marks,
        assignment,
        final_marks
    ])

df = pd.DataFrame(data, columns=[
    "ATTENDENCE",
    "STUDY HOURS",
    "PREVIOUS MARKS",
    "ASSIGNMENT COMPLETION",
    "FINAL MARKS"
])

df.to_excel("student_data_500.xlsx", index=False)

print("500 student records created!")
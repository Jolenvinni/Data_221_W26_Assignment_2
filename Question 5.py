"""
Question 5

Here you will create a new categorical variable and generate a grouped summary table.
Using student.csv:
• Create a new column grade_band:
– Low: grade ≤ 9
– Medium: grade 10–14
– High: grade ≥ 15

• Create a grouped summary table showing for each band:
– number of students
– average absences
– percentage of students with internet access

• Save the table as student_bands.csv.

"""
import pandas as pd
import numpy as np

# 1.) Create a new column grade_band.
student_data = pd.read_csv("student.csv", delimiter=",")

grade_band = [
    (student_data["grade"] >= 15),
    (student_data["grade"] > 9) & (student_data["grade"] < 15),
    (student_data["grade"] <= 9),
]
grade_level = ["High", "Medium", "Low"]

student_data["grade_band"] = np.select(grade_band, grade_level, default = "Unavailable")


# 2.) Create a grouped summary table showing for each band
grouped_summary_data = {
    "Number of students" : [
        len(student_data[student_data["grade_band"]=="High"]),
        len(student_data[student_data["grade_band"]=="Medium"]),
        len(student_data[student_data["grade_band"]=="Low"])
    ],
    "Average absences" : [
        student_data[student_data["grade_band"]=="High"]["grade"].mean(),
        student_data[student_data["grade_band"]=="Medium"]["grade"].mean(),
        student_data[student_data["grade_band"]=="Low"]["grade"].mean()
    ],
    "Percentage of students with internet access" : [
        student_data[student_data["grade_band"]=="High"]["internet"].mean(),
        student_data[student_data["grade_band"]=="Medium"]["internet"].mean(),
        student_data[student_data["grade_band"]=="Low"]["internet"].mean()
    ]
}

grouped_summary_table = pd.DataFrame(grouped_summary_data, index = ["High", "Medium", "Low"])

# 3.) Save the table as student_bands.csv.
grouped_summary_table.to_csv("student_bands.csv")
print("Grouped summary table saved to student_bands.csv.")
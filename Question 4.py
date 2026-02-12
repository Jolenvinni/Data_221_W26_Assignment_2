"""
Question 4

This question involves filtering tabular data and saving the results to a new file.
Using student.csv:
• Load the dataset into a DataFrame.
• Filter students where studytime ≥ 3, internet = 1, and absences ≤ 5.
• Save the filtered data to high_engagement.csv.
• Print the number of students saved and their average grade.

"""

import pandas as pd

# 1.) Load the dataset into a DataFrame.
student_data = pd.read_csv('student.csv', delimiter=',')

# 2.) Filter students where studytime ≥ 3, internet = 1, and absences ≤ 5.
filtered_student_data = student_data[(student_data['studytime'] >= 3) & (student_data['internet'] == 1) & (student_data['absences'] <= 5)]

 # 3.) Save the filtered data to high_engagement.csv.
filtered_student_data.to_csv("high_engagement.csv")
print("saved filtered data to high_engagement.csv")

# 4.) Print the number of students saved and their average grade.
number_of_filtered_students = len(filtered_student_data)
filtered_average_grade = filtered_student_data['grade'].mean()

print(f"Number of students saved: {number_of_filtered_students} \nAverage grade: {filtered_average_grade:.4f}")
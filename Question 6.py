"""
Question 6

In this question, you will create a simple category based on crime levels and compare unem-
ployment rates between the groups.
Using crime.csv:
• Load the dataset into a pandas DataFrame.
• Create a new column called risk based on ViolentCrimesPerPop:
– If ViolentCrimesPerPop is greater than or equal to 0.50, set risk = "High-
Crime".
– Otherwise, set risk = "LowCrime".
• Group the data by the risk column.
• For each group, calculate the average value of PctUnemployed.
• Print the average unemployment rate for both HighCrime and LowCrime groups in a
clear format

"""
import pandas as pd
import numpy as np

# 1.) Load the dataset into a pandas DataFrame.
crime_data = pd.read_csv("crime.csv", delimiter=",")


# 2.) Create a new column called risk based on ViolentCrimesPerPop.
conditions_for_risk_level = [
    (crime_data["ViolentCrimesPerPop"] >= 0.50),
    (crime_data["ViolentCrimesPerPop"] < 0.50)
]

risk_level = ["HighCrime", "LowCrime"]

crime_data["risk based on ViolentCrimesPerPop"] = (
    np.select(conditions_for_risk_level, risk_level, default = "Unavailable"))


# 3.) Group the data by the risk column.
high_crime_data = crime_data[crime_data["risk based on ViolentCrimesPerPop"]=="HighCrime"]
low_crime_data = crime_data[crime_data["risk based on ViolentCrimesPerPop"]=="LowCrime"]


# 4.) For each group, calculate the average value of PctUnemployed.
high_crime_pct_unemployed = high_crime_data["PctUnemployed"].mean()
low_crime_pct_unemployed = low_crime_data["PctUnemployed"].mean()


# 5.) Print the average unemployment rate for both HighCrime and LowCrime groups in a
# clear format.
print(f"Average unemployment rate for HighCrime group: {high_crime_pct_unemployed:.4f}")
print(f"Average unemployment rate for LowCrime group: {low_crime_pct_unemployed:.4f}")
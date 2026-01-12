# Health Risk Analysis Using NumPy, Pandas, Matplotlib (Real-Life Scenario)

# Domain - Medical and Health Sciences / Health Data Analytics

# Problem Statement (Real-Life Context)

# A primary healthcare center collects basic health screening data from adults during annual checkups. The objective is to identify individuals at risk of lifestyle diseases (such as diabetes and hypertension) using numerical health indicators.

# The healthcare team wants:

    # Fast numerical computation
    # Vectorized analysis (no loops)
    # Summary statistics for decision-making

# Why Extend NumPy → Pandas + Visualization

# NumPy → efficient numerical computation Pandas → tabular health data management Visualization → clinical and policy-level decision support

# This mirrors real healthcare analytics workflows.

# Dataset Description

# Each patient record contains:

# Column	                   Description
# Age	                           Patient age (years)
# BMI	                           Body Mass Index
# Systolic_BP	               	   Blood pressure (mmHg)
# Fasting_Glucose	           Blood sugar level (mg/dL)

# Implementation

# Step 1. Import required libraries, Create Health dataset using Pandas, Convert NumPy Array to DataFrame

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# patient health data
# Columns: Age, BMI, Systolic_BP, Fasting_Glucose

health_data = np.array([
    [25, 22.4, 118, 90], # health record of patient 1
    [32, 27.8, 130, 110], # health record of patient 2
    [45, 29.5, 142, 135], # health record of patient 3
    [50, 31.2, 150, 160], # health record of patient 4
    [29, 24.1, 120, 95], # health record of patient 5
    [60, 33.5, 155, 180], # health record of patient 6
    [41, 28.9, 138, 125], # health record of patient 7
    [36, 26.3, 132, 105], # health record of patient 8
    [55, 34.1, 160, 190], # health record of patient 9
    [48, 30.8, 145, 155], # health record of patient 10
    [39, 27.0, 135, 115], # health record of patient 11
    [65, 35.2, 165, 200], # health record of patient 12
    [28, 23.5, 122, 92], # health record of patient 13
    [52, 32.6, 148, 170], # health record of patient 14
    [46, 29.9, 140, 140], # health record of patient 15
    [34, 25.8, 128, 100], # health record of patient 16
    [58, 33.9, 158, 185], # health record of patient 17
    [43, 28.1, 137, 120], # health record of patient 18
    [31, 26.5, 130, 108], # health record of patient 19
    [49, 31.0, 150, 165] # health record of patient 20
])

columns = ['Age', 'BMI', 'Systolic_BP', 'Fasting_Glucose']

df = pd.DataFrame(health_data, columns=columns)
print(df.head())

# Exploratory Data Analysis (EDA)

# Step 2: Summary Statistics

print(df.describe())

# Healthcare use: 1. Identifies abnormal averages. 2. Supports population health profiling

# Add Risk Classification (Clinical Logic)

# Step 3: Create Risk Columns

df['Obesity_Risk'] = df['BMI'] >= 30
df['Hypertension_Risk'] = df['Systolic_BP'] >= 140
df['Diabetes_Risk'] = df['Fasting_Glucose'] >= 126

# Step 4: Overall Risk Flag

df['High_Risk'] = (
    df['Obesity_Risk'] |
    df['Hypertension_Risk'] |
    df['Diabetes_Risk']
)
print(df[['Age', 'BMI', 'Systolic_BP', 'Fasting_Glucose', 'High_Risk']].head())

# Visualization 1 – Distribution of BMI

plt.figure()
plt.hist(df['BMI'], bins=8)
plt.xlabel("BMI")
plt.ylabel("Number of Patients")
plt.title("BMI Distribution")
plt.show()

# Interpretation: Identifies obesity prevalence in the population.

# Visualization 2 – Age vs Glucose Scatter Plot

plt.figure()
plt.scatter(df['Age'], df['Fasting_Glucose'])
plt.xlabel("Age")
plt.ylabel("Fasting Glucose")
plt.title("Age vs Fasting Glucose Levels")
plt.show()

# Clinical insight: Shows increased glucose levels with age.

# Visualization 3 – Risk Category Counts (Bar Chart)

risk_counts = [
    df['Obesity_Risk'].sum(),
    df['Hypertension_Risk'].sum(),
    df['Diabetes_Risk'].sum()
]

labels = ['Obesity', 'Hypertension', 'Diabetes']

plt.figure()
plt.bar(labels, risk_counts)
plt.xlabel("Risk Type")
plt.ylabel("Number of Patients")
plt.title("Health Risk Distribution")
plt.show()

# Policy relevance: Helps prioritize preventive health programs.

# Visualization 4 – High-Risk vs Low-Risk Patients

risk_summary = df['High_Risk'].value_counts()

plt.figure()
plt.pie(
    risk_summary,
    labels=['High Risk', 'Low Risk'],
    autopct='%1.1f%%'
)
plt.title("Overall Risk Distribution")
plt.show()


# Key Insights:
# 1. Pandas simplifies health data management
# 2. Visualization enables quick clinical interpretation
# 3. Identifies high-risk populations effectively
# 4. Scales easily to thousands of patient records

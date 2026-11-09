# -*- coding: utf-8 -*-
"""
Author: Aaryan Samanta

Organization: Legend College Preparatory

Date: 2025

Title: symptoms

Version: 1.0

Type: Source Code

Adaptation details: Based on classroom exercises

Disclaimer: Developed as part of the AI Internship at Legend College Preparatory. Please note that it is a violation of school policy 
to copy and use this code without proper attribution and credit acknowledgement. Failing to do so can constitute plagiarism, even with small code snippets.

"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load
df = pd.read_csv("Disease_Symptom_and_Patient_Profile_Dataset.csv")

# Initial check
print(df.head())
print(df.isnull().sum())

df = df.drop_duplicates()

df["Age"] = pd.to_numeric(df["Age"], errors="coerce").fillna(0)

df["Gender"] = df["Gender"].astype("category")

if "Blood Pressure" in df.columns:
    if df["Blood Pressure"].dtype == "object":
        df["Blood Pressure"] = df["Blood Pressure"].astype("category").cat.codes
    else:
        df["Blood Pressure"] = pd.to_numeric(df["Blood Pressure"], errors="coerce").fillna(0)

if "Cholesterol Level" in df.columns:
    if df["Cholesterol Level"].nunique() == 0:
        df = df.drop(columns=["Cholesterol Level"])
    else:
        if df["Cholesterol Level"].dtype == "object":
            df["Cholesterol Level"] = df["Cholesterol Level"].astype("category").cat.codes
        else:
            df["Cholesterol Level"] = pd.to_numeric(df["Cholesterol Level"], errors="coerce").fillna(0)

print(df.info())

print(df.describe(include="all"))

print(df.median(numeric_only=True))

print(df.std(numeric_only=True))

plt.figure(figsize=(8,5))
sns.histplot(df["Age"], bins=20, kde=True)
plt.title("Age Distribution")
plt.show()

if "Blood Pressure" in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df["Blood Pressure"], bins=15, kde=True)
    plt.title("Blood Pressure Distribution")
    plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x="Gender", y="Age", data=df)
plt.title("Age by Gender")
plt.show()

if "Blood Pressure" in df.columns:
    plt.figure(figsize=(8,5))
    sns.boxplot(x="Gender", y="Blood Pressure", data=df)
    plt.title("Blood Pressure by Gender")
    plt.show()

top_diseases = df["Disease"].value_counts().head(20).index
plt.figure(figsize=(10,8))
sns.countplot(y="Disease", data=df[df["Disease"].isin(top_diseases)], order=top_diseases)
plt.title("Top 20 Diseases")
plt.show()

numeric_df = df.select_dtypes(include=[np.number])
plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

import pandas as pd

# Load the dataset
df = pd.read_csv("students.csv")

print("DATA QUALITY REPORT")
print("===================")

# Basic information
print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(list(df.columns))

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Sample data
print("\nFirst 5 Rows:")
print(df.head())
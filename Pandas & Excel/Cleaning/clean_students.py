import pandas as pd

# Load the messy dataset
df = pd.read_csv("messy_students.csv")

print("ORIGINAL DATA")
print("-------------")
print(df)

# 1. Remove extra spaces from text columns
df["Name"] = df["Name"].str.strip()
df["City"] = df["City"].str.strip()

# 2. Standardize city names
df["City"] = df["City"].str.title()

# 3. Convert numeric columns to numbers
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# 4. Fill missing numeric values with median
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Marks"] = df["Marks"].fillna(df["Marks"].median())

# 5. Convert dates to a consistent format
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")

# 6. Remove duplicate rows
df = df.drop_duplicates()

print("\nCLEANED DATA")
print("------------")
print(df)

# 7. Check remaining missing values
print("\nMISSING VALUES AFTER CLEANING")
print("-----------------------------")
print(df.isnull().sum())

# 8. Check data types
print("\nDATA TYPES AFTER CLEANING")
print("-------------------------")
print(df.dtypes)

# 9. Validate Marks
print("\nVALIDATION")
print("----------")

if df["Marks"].between(0, 100).all():
    print("Marks validation: Passed")
else:
    print("Marks validation: Failed")

# 10. Validate Age
if df["Age"].between(1, 100).all():
    print("Age validation: Passed")
else:
    print("Age validation: Failed")

# 11. Check duplicates
if df.duplicated().sum() == 0:
    print("Duplicate validation: Passed")
else:
    print("Duplicate validation: Failed")

# 12. Save cleaned dataset
df.to_csv("cleaned_students.csv", index=False)

print("\nCleaned dataset saved as cleaned_students.csv")
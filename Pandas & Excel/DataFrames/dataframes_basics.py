import pandas as pd

# Series
ages = pd.Series([21, 22, 23])

print("Series:")
print(ages)

# DataFrame
data = {
    "Name": ["Vyshnavi", "Charan", "Rahul"],
    "Age": [21, 22, 23]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)
students = pd.read_csv("students.csv")

print("\nCSV Data:")
print(students)
print("\nData Types:")
print(students.dtypes)
print("\nName Column:")
print(students["Name"])
print("\nName and Marks:")
print(students[["Name", "Marks"]])
print("\nFirst Row:")
print(students.iloc[0])
print("\nFirst Three Rows:")
print(students.iloc[0:3])
print("\nFirst 5 Rows:")
print(students.head())

print("\nLast 5 Rows:")
print(students.tail())

print("\nShape:")
print(students.shape)

print("\nColumns:")
print(students.columns)

print("\nInfo:")
students.info()

print("\nDescription:")
print(students.describe())
\# Data Cleaning



\## Overview



This module demonstrates repeatable data-cleaning logic using Pandas.



A deliberately messy student dataset was created with missing values,

duplicate records, inconsistent text formatting, and inconsistent date

values.



\## Cleaning Operations



\### 1. String Normalization



Leading and trailing spaces were removed from `Name` and `City`.



City names were standardized using title case.



\### 2. Type Conversion



`Age` and `Marks` were converted to numeric values.



Invalid numeric values were converted to missing values using

`errors="coerce"`.



\### 3. Missing Values



Missing `Age` and `Marks` values were filled using the median of their

respective columns.



\### 4. Date Normalization



`Join\_Date` was converted to a Pandas datetime type.



Invalid date values were converted to missing values.



\### 5. Duplicate Removal



Duplicate rows were identified and removed using `drop\_duplicates()`.



\### 6. Validation



The cleaned data was validated to check:



\- Marks are between 0 and 100.

\- Age values are within a reasonable range.

\- No duplicate rows remain.



\## Assumptions



\- Missing numeric values are replaced with the column median.

\- Student marks must be between 0 and 100.

\- Age values must be between 1 and 100.

\- Duplicate records are removed when all column values are identical.

\- City names are standardized using title case.

\- Invalid dates are treated as missing values.



\## Files



```text

Cleaning/

├── messy\_students.csv

├── clean\_students.py

├── cleaned\_students.csv

└── README.md


# DataFrames

## Overview

This module introduces Pandas DataFrames for working with structured tabular data.

## Topics Covered

- Series
- DataFrame
- Loading CSV data
- Data types using `dtypes`
- Column selection
- Row indexing using `iloc`
- DataFrame inspection
- Basic data-quality reporting

## Dataset

The practice dataset is `students.csv`.

It contains the following columns:

- Name
- Age
- City
- Marks

## Data Inspection

The following Pandas methods were practiced:

- `head()` – view the first rows
- `tail()` – view the last rows
- `shape` – get rows and columns
- `columns` – view column names
- `dtypes` – check data types
- `info()` – inspect DataFrame structure
- `describe()` – view numerical summary

## Data Quality Report

The `data_quality_report.py` script checks:

- Dataset shape
- Column names
- Data types
- Missing values
- Duplicate rows
- Sample records

## Files

```text
DataFrames/
├── dataframes_basics.py
├── data_quality_report.py
├── students.csv
└── README.md
# Pandas & Excel – Independent Challenge

## Overview

This project implements a reusable Excel-to-report pipeline using Python
and OpenPyXL.

The pipeline reads Excel data, validates the input, performs sales
transformations, generates summary information, and produces a structured
Excel report. It also includes test fixtures and an error summary sheet
for identifying invalid data.

## Objectives

- Build a reusable Excel processing pipeline
- Validate input data before processing
- Perform sales calculations and transformations
- Generate summary reports
- Identify and document validation errors
- Produce a structured Excel output workbook
- Use separate test fixtures for valid and invalid data

## Technologies Used

- Python
- OpenPyXL
- Microsoft Excel

## Project Structure

```text
Independent Challenge/
│
├── input/
│   ├── create_input.py
│   ├── sales_input.xlsx
│   └── valid_sales_input.xlsx
│
├── output/
│   └── sales_report.xlsx
│
├── tests/
│   └── valid_input.py
│
├── pipeline.py
└── README.md
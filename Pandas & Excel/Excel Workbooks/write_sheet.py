import openpyxl

# Open the existing workbook
workbook = openpyxl.load_workbook("sales_data.xlsx")

# Create a new worksheet
summary = workbook.create_sheet("Summary")

# Write data into the sheet
summary["A1"] = "Sales Summary"
summary["A2"] = "Total Orders"
summary["B2"] = 6

summary["A3"] = "Total Sales"
summary["B3"] = 188000

# Save the updated workbook
workbook.save("sales_data.xlsx")

print("Summary sheet created successfully.")
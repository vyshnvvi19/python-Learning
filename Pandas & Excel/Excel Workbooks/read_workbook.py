import openpyxl

# Open the existing workbook
workbook = openpyxl.load_workbook("sales_data.xlsx")

# Show all sheet names
print("Sheets:")
print(workbook.sheetnames)

# Select the Sales sheet
sales = workbook["Sales"]

# Read the first cell
print("\nFirst Cell:")
print(sales["A1"].value)

# Read the first data row
print("\nFirst Data Row:")
for cell in sales[2]:
    print(cell.value)
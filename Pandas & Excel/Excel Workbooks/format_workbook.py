import openpyxl
from openpyxl.styles import Font, Alignment

workbook = openpyxl.load_workbook("sales_data.xlsx")

sales = workbook["Sales"]
summary = workbook["Summary"]

# Format Sales header
for cell in sales[1]:
    cell.font = Font(bold=True)
    cell.alignment = Alignment(horizontal="center")

# Format Summary header
summary["A1"].font = Font(bold=True, size=14)

for cell in summary[2]:
    cell.font = Font(bold=True)

# Set column widths
sales.column_dimensions["A"].width = 12
sales.column_dimensions["B"].width = 15
sales.column_dimensions["C"].width = 12
sales.column_dimensions["D"].width = 12
sales.column_dimensions["E"].width = 15
sales.column_dimensions["F"].width = 15

summary.column_dimensions["A"].width = 20
summary.column_dimensions["B"].width = 18

# Number formatting
for row in range(2, sales.max_row + 1):
    sales[f"D{row}"].number_format = '#,##0'
    sales[f"F{row}"].number_format = '#,##0'

summary["B5"].number_format = '#,##0'
summary["B6"].number_format = '#,##0.00'

workbook.save("sales_data.xlsx")

print("Workbook formatted successfully.")
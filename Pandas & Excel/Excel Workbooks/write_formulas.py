import openpyxl

workbook = openpyxl.load_workbook("sales_data.xlsx")

sales = workbook["Sales"]
summary = workbook["Summary"]

# Add a Total Sales column
sales["F1"] = "Total Sales"

# Formula for each sales row
for row in range(2, sales.max_row + 1):
    sales[f"F{row}"] = f"=C{row}*D{row}"

# Add summary formulas
summary["A5"] = "Total Sales"
summary["B5"] = "=SUM(Sales!F2:F7)"

summary["A6"] = "Average Sale"
summary["B6"] = "=AVERAGE(Sales!F2:F7)"

workbook.save("sales_data.xlsx")

print("Formulas added successfully.")
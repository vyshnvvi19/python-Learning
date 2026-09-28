import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Sales"

sheet.append(["Order_ID", "Product", "Quantity", "Price", "City"])

sheet.append(["ORD001", "Laptop", 2, 50000, "Hyderabad"])
sheet.append(["ORD002", "Mouse", 5, 800, "Hyderabad"])
sheet.append(["ORD003", "Chair", 4, 3000, "Warangal"])
sheet.append(["ORD004", "Laptop", 1, 50000, "Hyderabad"])
sheet.append(["ORD004", "Desk", 2, 7000, "Karimnagar"])
sheet.append(["ORD006", "", 10, 800, "Warangal"])

workbook.save("sales_input.xlsx")

print("Input Excel file created successfully.")
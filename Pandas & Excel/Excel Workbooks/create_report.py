import openpyxl

# Create a new workbook
workbook = openpyxl.Workbook()

# Create Sales sheet
sales = workbook.active
sales.title = "Sales"

sales.append(["Order_ID", "Product", "Quantity", "Price", "City"])
sales.append(["ORD001", "Laptop", 2, 50000, "Hyderabad"])
sales.append(["ORD002", "Mouse", 5, 800, "Hyderabad"])
sales.append(["ORD003", "Chair", 4, 3000, "Warangal"])
sales.append(["ORD004", "Laptop", 1, 50000, "Hyderabad"])
sales.append(["ORD005", "Desk", 2, 7000, "Karimnagar"])
sales.append(["ORD006", "Mouse", 10, 800, "Warangal"])

# Create Products sheet
products = workbook.create_sheet("Products")

products.append(["Product", "Category", "Supplier"])
products.append(["Laptop", "Electronics", "Dell"])
products.append(["Mouse", "Electronics", "Logitech"])
products.append(["Chair", "Furniture", "Nilkamal"])
products.append(["Desk", "Furniture", "Featherlite"])

# Save workbook
workbook.save("sales_data.xlsx")

print("Excel workbook created successfully.")
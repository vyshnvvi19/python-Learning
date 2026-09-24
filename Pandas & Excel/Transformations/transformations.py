import pandas as pd

# Load sales data
sales = pd.read_csv("sales.csv")

# Convert Date to datetime
sales["Date"] = pd.to_datetime(sales["Date"])

print("ORIGINAL DATA")
print(sales)

# 1. Calculated column
sales["Total_Sales"] = sales["Quantity"] * sales["Price"]

print("\nCALCULATED COLUMN")
print(sales[["Product", "Quantity", "Price", "Total_Sales"]])

# 2. Filter
high_value_sales = sales[sales["Total_Sales"] >= 10000]

print("\nFILTERED SALES")
print(high_value_sales)

# 3. Sort
sorted_sales = sales.sort_values("Total_Sales", ascending=False)

print("\nSORTED SALES")
print(sorted_sales[["Product", "Total_Sales"]])

# 4. Groupby
city_sales = sales.groupby("City")["Total_Sales"].sum()

print("\nSALES BY CITY")
print(city_sales)

# 5. Aggregate
product_summary = sales.groupby("Product")["Total_Sales"].agg(
    ["count", "sum", "mean", "max"]
)

print("\nPRODUCT SUMMARY")
print(product_summary)

# 6. Merge / Join
products = pd.read_csv("products.csv")

merged_data = pd.merge(
    sales,
    products,
    on=["Product", "Category"],
    how="left"
)

print("\nMERGED DATA")
print(merged_data)

# 7. Monthly summary
sales["Month"] = sales["Date"].dt.to_period("M")

monthly_summary = sales.groupby("Month")["Total_Sales"].sum()

print("\nMONTHLY SALES SUMMARY")
print(monthly_summary)

# 8. Pivot table
pivot_report = pd.pivot_table(
    sales,
    values="Total_Sales",
    index="Month",
    columns="City",
    aggfunc="sum",
    fill_value=0
)

print("\nPIVOT REPORT")
print(pivot_report)
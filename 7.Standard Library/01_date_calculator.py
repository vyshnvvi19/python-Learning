from datetime import date
start = input("Enter start date (YYYY-MM-DD): ")
end = input("Enter end date (YYYY-MM-DD): ")

start_date = date.fromisoformat(start)
end_date = date.fromisoformat(end)

difference = end_date - start_date

print("Start Date:", start_date)
print("End Date:", end_date)
print("Difference:", difference.days, "days")
employees = {
    "E01": {"name": "Anu", "age": 22, "salary": 30000},
    "E02": {"name": "Ravi", "age": 24, "salary": 35000},
    "E03": {"name": "Priya", "age": 23, "salary": 32000}
}
emp_id = input("Enter employee ID: ")
if emp_id in employees:
    print("Name:", employees[emp_id]["name"])
    print("Age:", employees[emp_id]["age"])
    print("Salary:", employees[emp_id]["salary"])
else:
    print("Employee not found")
import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Students"

sheet.append(["Student_ID", "Name", "Age", "Marks"])

sheet.append(["STU001", "Vyshnavi", 21, 85])
sheet.append(["STU002", "Charan", 22, 78])
sheet.append(["STU002", "Rahul", 23, 105])
sheet.append(["STU004", "", 20, 92])
sheet.append(["STU005", "Anu", 150, 88])

workbook.save("students.xlsx")

print("Test Excel file created successfully.")
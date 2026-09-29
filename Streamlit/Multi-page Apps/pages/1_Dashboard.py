import streamlit as st

from components.student_summary import show_student_summary


st.title("Student Management System")

st.header("Dashboard")

st.write(
    "Welcome to the Student Management System."
)


students = [
    {
        "Name": "Vyshnavi",
        "Course": "Python",
        "Marks": 85
    },
    {
        "Name": "Charan",
        "Course": "Data Science",
        "Marks": 78
    },
    {
        "Name": "Rahul",
        "Course": "Python",
        "Marks": 92
    },
    {
        "Name": "Anu",
        "Course": "Java",
        "Marks": 88
    },
    {
        "Name": "Kiran",
        "Course": "Data Science",
        "Marks": 76
    },
    {
        "Name": "Sneha",
        "Course": "Python",
        "Marks": 89
    }
]


show_student_summary(students)


st.subheader("Student Overview")

st.dataframe(
    students,
    use_container_width=True
)


st.subheader("Marks Overview")

marks_data = {
    student["Name"]: student["Marks"]
    for student in students
}

st.bar_chart(marks_data)
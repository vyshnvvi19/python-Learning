import streamlit as st


st.title("Students")

st.header("Student Records")

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


search_name = st.text_input("Search student by name")


filtered_students = students

if search_name:
    filtered_students = [
        student
        for student in students
        if search_name.lower() in student["Name"].lower()
    ]


st.subheader("Student List")

st.dataframe(
    filtered_students,
    use_container_width=True
)

st.write("Students found:", len(filtered_students))
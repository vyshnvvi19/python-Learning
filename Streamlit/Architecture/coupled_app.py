import streamlit as st


st.set_page_config(
    page_title="Student Management",
    page_icon="🎓"
)


st.title("🎓 Student Management")


# -------------------------
# STUDENT DATA
# -------------------------

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
    }
]


# -------------------------
# ADD STUDENT
# -------------------------

st.subheader("Add Student")

name = st.text_input(
    "Student Name"
)

course = st.selectbox(
    "Course",
    [
        "Python",
        "Java",
        "Data Science"
    ]
)

marks = st.number_input(
    "Marks",
    min_value=0,
    max_value=100,
    value=0
)


if st.button("Add Student"):

    # Validation
    if not name.strip():

        st.error(
            "Student name is required."
        )

    elif marks <= 0:

        st.error(
            "Marks must be greater than 0."
        )

    else:

        # Create student
        student = {
            "Name": name.strip(),
            "Course": course,
            "Marks": marks
        }

        # Store student
        students.append(student)

        st.success(
            f"{name.strip()} added successfully."
        )


# -------------------------
# DISPLAY STUDENTS
# -------------------------

st.subheader("Student Records")

st.dataframe(
    students,
    use_container_width=True
)
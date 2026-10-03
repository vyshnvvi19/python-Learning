import streamlit as st

from repositories.student_repository import StudentRepository
from services.student_service import StudentService


st.set_page_config(
    page_title="Student Management",
    page_icon="🎓"
)


st.title("🎓 Student Management")


# -------------------------
# CREATE SERVICE
# -------------------------

repository = StudentRepository()
service = StudentService(repository)


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

    try:

        service.add_student(
            name,
            course,
            marks
        )

        st.success(
            f"{name.strip()} added successfully."
        )

    except ValueError as error:

        st.error(str(error))


# -------------------------
# DISPLAY STUDENTS
# -------------------------

st.subheader("Student Records")

students = service.get_students()

st.dataframe(
    students,
    use_container_width=True
)
import streamlit as st

from config.settings import COURSES, MAX_MARKS

st.title("Manage Students")

st.header("Student Management")


# Initialize student data
if "students" not in st.session_state:
    st.session_state.students = [
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
        }
    ]


# -------------------------
# CREATE
# -------------------------

st.subheader("Add Student")

with st.form("add_student_form"):

    name = st.text_input("Student Name")

    course = st.selectbox(
        "Course",
        ["Python", "Java", "Data Science"]
    )

    marks = st.number_input(
        "Marks",
        min_value=0,
        max_value=100,
        value=0
    )

    submitted = st.form_submit_button("Add Student")

    if submitted:

        if not name.strip():
            st.error("Student name is required.")

        else:
            st.session_state.students.append(
                {
                    "Name": name,
                    "Course": course,
                    "Marks": marks
                }
            )

            st.success(
                f"Student {name} added successfully."
            )


# -------------------------
# UPDATE
# -------------------------

st.subheader("Update Student")

student_names = [
    student["Name"]
    for student in st.session_state.students
]

if student_names:

    selected_student = st.selectbox(
        "Select student to update",
        student_names
    )

    selected_index = student_names.index(selected_student)

    current_course = st.session_state.students[
        selected_index
    ]["Course"]

    current_marks = st.session_state.students[
        selected_index
    ]["Marks"]

    new_course = st.selectbox(
        "Update Course",
        ["Python", "Java", "Data Science"],
        index=[
            "Python",
            "Java",
            "Data Science"
        ].index(current_course)
    )

    new_marks = st.number_input(
        "Update Marks",
        min_value=0,
        max_value=100,
        value=current_marks
    )

    if st.button("Update Student"):

        st.session_state.students[
            selected_index
        ]["Course"] = new_course

        st.session_state.students[
            selected_index
        ]["Marks"] = new_marks

        st.success(
            f"{selected_student} updated successfully."
        )


# -------------------------
# DELETE
# -------------------------

st.subheader("Delete Student")

student_names = [
    student["Name"]
    for student in st.session_state.students
]

if student_names:

    student_to_delete = st.selectbox(
        "Select student to delete",
        student_names,
        key="delete_student"
    )

    if st.button("Delete Student"):

        delete_index = student_names.index(
            student_to_delete
        )

        st.session_state.students.pop(
            delete_index
        )

        st.success(
            f"{student_to_delete} deleted successfully."
        )


# -------------------------
# DISPLAY STUDENTS
# -------------------------

st.subheader("Student Records")

st.dataframe(
    st.session_state.students,
    use_container_width=True
)
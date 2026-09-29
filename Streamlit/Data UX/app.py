import streamlit as st
import pandas as pd


# -------------------------
# PAGE CONFIGURATION
# -------------------------

st.set_page_config(
    page_title="Student Data Report",
    page_icon="📊",
    layout="wide"
)


# -------------------------
# PAGE TITLE
# -------------------------

st.title("📊 Student Data Report")

st.write(
    "Add, view, filter, validate, and download student records."
)


# -------------------------
# INITIAL STUDENT DATA
# -------------------------

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


# -------------------------
# ADD STUDENT
# -------------------------

st.subheader("➕ Add Student")

with st.form("add_student_form"):

    student_name = st.text_input(
        "Student Name"
    )

    student_course = st.selectbox(
        "Course",
        [
            "Python",
            "Java",
            "Data Science"
        ]
    )

    student_marks = st.number_input(
        "Marks",
        min_value=0,
        max_value=100,
        value=0
    )

    add_student = st.form_submit_button(
        "Add Student"
    )


if add_student:

    if not student_name.strip():

        st.error(
            "Student name is required."
        )

    elif student_marks == 0:

        st.warning(
            "Please enter valid marks."
        )

    else:

        st.session_state.students.append(
            {
                "Name": student_name.strip(),
                "Course": student_course,
                "Marks": student_marks
            }
        )

        st.success(
            f"{student_name.strip()} added successfully."
        )


# -------------------------
# SEARCH AND FILTER
# -------------------------

st.subheader("🔎 Search and Filter Students")

col1, col2 = st.columns(2)


with col1:

    search_name = st.text_input(
        "Search student by name"
    )


with col2:

    selected_course = st.selectbox(
        "Filter by course",
        [
            "All",
            "Python",
            "Java",
            "Data Science"
        ]
    )


# Start with all students
filtered_students = st.session_state.students


# Apply name search
if search_name:

    filtered_students = [
        student
        for student in filtered_students
        if search_name.lower()
        in student["Name"].lower()
    ]


# Apply course filter
if selected_course != "All":

    filtered_students = [
        student
        for student in filtered_students
        if student["Course"] == selected_course
    ]


# -------------------------
# RESULT COUNT
# -------------------------

st.write(
    f"Students found: {len(filtered_students)}"
)


# -------------------------
# MARKS VALIDATION
# -------------------------

st.subheader("✅ Marks Validation")

marks_to_check = st.number_input(
    "Enter marks to validate",
    min_value=0,
    max_value=150,
    value=0
)


if st.button("Validate Marks"):

    if marks_to_check > 100:

        st.error(
            "Invalid marks. Marks must be between 0 and 100."
        )

    elif marks_to_check == 0:

        st.warning(
            "Marks are currently set to 0."
        )

    else:

        st.success(
            "Marks are valid."
        )


# -------------------------
# STUDENT TABLE
# -------------------------

st.subheader("📋 Student Records")


if filtered_students:

    st.dataframe(
        filtered_students,
        use_container_width=True
    )

else:

    st.info(
        "No students found for the selected search and filter."
    )


# -------------------------
# DOWNLOAD DATA
# -------------------------

if filtered_students:

    df = pd.DataFrame(
        filtered_students
    )

    csv_data = df.to_csv(
        index=False
    )

    st.download_button(
        label="⬇️ Download CSV",
        data=csv_data,
        file_name="student_report.csv",
        mime="text/csv"
    )
import streamlit as st


def show_student_summary(students):

    total_students = len(students)

    if total_students > 0:
        average_marks = sum(
            student["Marks"]
            for student in students
        ) / total_students
    else:
        average_marks = 0

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Students",
            total_students
        )

    with col2:
        st.metric(
            "Average Marks",
            round(average_marks, 2)
        )
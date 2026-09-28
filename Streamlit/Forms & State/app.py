import streamlit as st


if "step" not in st.session_state:
    st.session_state["step"] = 1

if "name" not in st.session_state:
    st.session_state["name"] = ""

if "age" not in st.session_state:
    st.session_state["age"] = 0

if "course" not in st.session_state:
    st.session_state["course"] = ""

if "learning_mode" not in st.session_state:
    st.session_state["learning_mode"] = ""


def go_to_step_two():
    name = st.session_state["form_name"].strip()
    age = st.session_state["form_age"]

    if not name:
        st.session_state["error"] = "Name is required."
        return

    if age <= 0:
        st.session_state["error"] = "Age must be greater than 0."
        return

    st.session_state["name"] = name
    st.session_state["age"] = age
    st.session_state["error"] = ""
    st.session_state["step"] = 2


def complete_registration():
    st.session_state["course"] = st.session_state["form_course"]
    st.session_state["learning_mode"] = st.session_state["form_mode"]
    st.session_state["step"] = 3


st.title("Student Registration")

if st.session_state["step"] == 1:

    st.header("Step 1: Student Details")

    with st.form("student_details_form"):
        st.text_input(
            "Enter your name",
            key="form_name"
        )

        st.number_input(
            "Enter your age",
            min_value=0,
            max_value=100,
            value=0,
            key="form_age"
        )

        st.form_submit_button(
            "Next",
            on_click=go_to_step_two
        )

    if "error" in st.session_state and st.session_state["error"]:
        st.error(st.session_state["error"])


elif st.session_state["step"] == 2:

    st.header("Step 2: Course Details")

    st.write("Name:", st.session_state["name"])
    st.write("Age:", st.session_state["age"])

    with st.form("course_details_form"):
        st.selectbox(
            "Select your course",
            ["Python", "Java", "Data Science"],
            key="form_course"
        )

        st.radio(
            "Select your learning mode",
            ["Online", "Offline"],
            key="form_mode"
        )

        st.form_submit_button(
            "Complete Registration",
            on_click=complete_registration
        )


elif st.session_state["step"] == 3:

    st.header("Registration Complete")

    st.success("Student registered successfully!")

    st.write("Name:", st.session_state["name"])
    st.write("Age:", st.session_state["age"])
    st.write("Course:", st.session_state["course"])
    st.write("Learning Mode:", st.session_state["learning_mode"])
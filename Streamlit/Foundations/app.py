import streamlit as st

st.title("Student Data Viewer")

st.write("View and explore student information.")

students = {
    "Name": ["Vyshnavi", "Charan", "Rahul", "Anu"],
    "Age": [21, 22, 23, 21],
    "Course": ["Python", "Data Science", "Python", "Java"],
    "Marks": [85, 78, 92, 88]
}

st.header("Student Filters")

name = st.text_input("Search student")

course = st.selectbox(
    "Select course",
    ["All", "Python", "Java", "Data Science"]
)

minimum_marks = st.slider(
    "Minimum marks",
    0,
    100,
    0
)

show_details = st.checkbox("Show student details")

filtered_students = students

if course != "All":
    filtered_students = {
        key: [
            value
            for i, value in enumerate(filtered_students[key])
            if filtered_students["Course"][i] == course
        ]
        for key in filtered_students
    }

if name:
    filtered_students = {
        key: [
            value
            for i, value in enumerate(filtered_students[key])
            if name.lower() in filtered_students["Name"][i].lower()
        ]
        for key in filtered_students
    }

filtered_students = {
    key: [
        value
        for i, value in enumerate(filtered_students[key])
        if filtered_students["Marks"][i] >= minimum_marks
    ]
    for key in filtered_students
}

st.header("Student Records")

st.dataframe(filtered_students)

if show_details and filtered_students["Name"]:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Students")
        st.write(len(filtered_students["Name"]))

    with col2:
        st.write("Average Marks")
        st.write(
            sum(filtered_students["Marks"])
            / len(filtered_students["Marks"])
        )

    with col3:
        st.write("Highest Marks")
        st.write(max(filtered_students["Marks"]))

st.header("Student Performance")

chart_data = {
    "Name": filtered_students["Name"],
    "Marks": filtered_students["Marks"]
}

st.bar_chart(
    chart_data,
    x="Name",
    y="Marks"
)
import streamlit as st
import pandas as pd

# --- Sample Data ---
students = pd.DataFrame({
    "Student ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Department": ["CSE", "ECE", "CSE"],
    "Group": ["A", "B", "A"],
    "Attendance (%)": [95, 88, 92],
    "Result": ["Pass", "Pass", "Fail"]
})

subjects = pd.DataFrame({
    "Subject Code": ["CS101", "EC201", "CS102"],
    "Subject Name": ["Python Programming", "Digital Circuits", "Data Structures"],
    "Department": ["CSE", "ECE", "CSE"],
    "Teacher": ["Dr. Smith", "Prof. Rao", "Dr. Lee"]
})

syllabus = {
    "CS101": "Introduction to Python, Data Types, Control Structures, Functions, Modules.",
    "EC201": "Logic Gates, Flip-Flops, Counters, Registers.",
    "CS102": "Arrays, Linked Lists, Stacks, Queues, Trees."
}

# --- Streamlit UI ---
st.title("EduPulse – Student Performance Dashboard")

st.header("Student Details")
st.dataframe(students)

st.header("Subjects & Teachers")
st.dataframe(subjects)

st.header("Syllabus")
subject_code = st.selectbox("Select Subject Code", subjects["Subject Code"])
st.write(f"**{subject_code} Syllabus:** {syllabus[subject_code]}")

st.header("Attendance Overview")
st.bar_chart(students.set_index("Name")["Attendance (%)"])

st.header("Results Overview")
result_counts = students["Result"].value_counts()
st.bar_chart(result_counts)
# ...existing code...

st.title("EduPulse – Student Performance Dashboard")

# --- Add New Student Form ---
st.header("Add New Student")
with st.form("add_student_form"):
    new_id = st.number_input("Student ID", min_value=1, step=1)
    new_name = st.text_input("Name")
    new_dept = st.selectbox("Department", students["Department"].unique())
    new_group = st.selectbox("Group", students["Group"].unique())
    new_attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, step=1)
    new_result = st.selectbox("Result", ["Pass", "Fail"])
    submitted = st.form_submit_button("Add Student")
    if submitted:
        new_row = {
            "Student ID": new_id,
            "Name": new_name,
            "Department": new_dept,
            "Group": new_group,
            "Attendance (%)": new_attendance,
            "Result": new_result
        }
        students.loc[len(students)] = new_row
        st.success(f"Added student: {new_name}")

# --- Student Details ---
st.header("Student Details")
st.dataframe(students)

# ...rest of your code...
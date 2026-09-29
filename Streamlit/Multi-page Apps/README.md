# Streamlit Multi-page Student Management System

## Overview

This project demonstrates the development of a structured multi-page web application using Streamlit.

The application implements a Student Management System with separate pages for dashboard visualization, student record management, and student search. It also demonstrates CRUD operations, session state, reusable components, and centralized configuration.

## Objectives

- Develop a multi-page Streamlit application
- Implement structured page navigation
- Apply Create, Read, Update, and Delete (CRUD) operations
- Manage application data using `st.session_state`
- Develop reusable UI components
- Centralize application-level configuration
- Follow a maintainable project structure

## Technologies Used

- **Python**
- **Streamlit**

## Project Structure

```text
Multi-page Apps/
│
├── app.py
│
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Students.py
│   └── 3_Manage_Students.py
│
├── components/
│   └── student_summary.py
│
├── config/
│   └── settings.py
│
└── README.md
import streamlit as st
import mysql.connector

def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    area = length * width
    return f'The Area = {area}'

def fibonacci_sequence(n):
    if n <= 0:
        return "Please enter a positive number."
    elif n == 1:
        return "0"
    
    a, b = 0, 1
    sequence = [a, b]

    for _ in range(2, n):
        a, b = b, a + b
        sequence.append(b)

    return " ".join(map(str, sequence))
config = {
    'user': 'project_ssd_intern',
    'password': 'asphalt@12A',
    'host': '127.0.0.1',
    'database': 'students'
}

def create_connection():
    return mysql.connector.connect(**config)

def setup_database_and_table():
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS your_database")
    cursor.execute("USE your_database")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            grade FLOAT NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

def insert_student(first_name, last_name, age, grade):
    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (first_name, last_name, age, grade))
    connection.commit()
    cursor.close()
    connection.close()

def update_student_grade(first_name, new_grade):
    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE students SET grade = %s WHERE first_name = %s"
    cursor.execute(query, (new_grade, first_name))
    connection.commit()
    cursor.close()
    connection.close()

def delete_student(last_name):
    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM students WHERE last_name = %s"
    cursor.execute(query, (last_name,))
    connection.commit()
    cursor.close()
    connection.close()

def fetch_all_students():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM students"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

st.title("Programming Tasks")

# Task 1: Calculate Area 
st.header("Task 1: Calculate Area with Conditions")
length = st.number_input("Enter length:", min_value=0)
width = st.number_input("Enter width:", min_value=0)
if st.button("Calculate Area"):
    result = calculate_area(length, width)
    st.write(result)

# Task 2: Generate Fibonacci Series
st.header("Task 2: Generate Fibonacci Series")
n = st.number_input("Enter the number of terms:", min_value=1)
if st.button("Generate Fibonacci Sequence"):
    result = fibonacci_sequence(n)
    st.write(result)

# Task 3: MySQL Database  Python
st.header("Task 3: MySQL Database Operations with Python")
st.write("Task 3 is not working online as I connected it with MySql LocalHost ,,")
if st.button("Setup Database and Table"):
    setup_database_and_table()
    st.write("Database and table created.")

if st.button("Insert Student Record"):
    insert_student("Alice", "Smith", 18, 95.5)
    st.write("Student record inserted.")

if st.button("Update Student Grade"):
    update_student_grade("Alice", 97.0)
    st.write("Student grade updated.")

if st.button("Delete Student Record"):
    delete_student("Smith")
    st.write("Student record deleted.")

if st.button("Fetch All Students"):
    students = fetch_all_students()
    for student in students:
        st.write(student)

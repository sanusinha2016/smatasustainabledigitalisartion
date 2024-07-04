

import mysql.connector

config = {
    'user': 'project_ssd_intern',
    'password': 'asphalt@12A',
    'host': '127.0.0.1',
    'database': 'studnets'
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
    for row in results:
        print(row)
    cursor.close()
    connection.close()

if __name__ == "__main__":
    setup_database_and_table()
    
    insert_student("Alice", "Smith", 18, 95.5)
    
    update_student_grade("Alice", 97.0)
    
    delete_student("Smith")
    
    fetch_all_students()

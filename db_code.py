# db_code.py

import mysql.connector

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_mysql_password"  # ← Change to your password
DB_NAME = "studentdb"

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            grade VARCHAR(10)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def create_student(name, age, grade):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)",
        (name, age, grade)
    )
    conn.commit()
    cursor.close()
    conn.close()

def create_students_bulk(students_list):
    """
    students_list: list of tuples [(name, age, grade), ...]
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"USE {DB_NAME}")
    cursor.executemany(
        "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)",
        students_list
    )
    conn.commit()
    cursor.close()
    conn.close()

def read_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def update_student(student_id, name, age, grade):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute(
        "UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s",
        (name, age, grade, student_id)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (student_id,)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute("DELETE FROM students")
    conn.commit()
    cursor.close()
    conn.close()

def search_students_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute(
        "SELECT * FROM students WHERE name LIKE %s",
        ('%' + name + '%',)
    )
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def list_students_by_grade(grade):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute(
        "SELECT * FROM students WHERE grade=%s",
        (grade,)
    )
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def show_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute(
        "SELECT * FROM students WHERE id=%s",
        (student_id,)
    )
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def count_total_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute("SELECT COUNT(*) FROM students")
    result = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return result

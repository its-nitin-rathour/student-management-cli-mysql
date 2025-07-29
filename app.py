# app.py

import os
from db_code import (
    initialize_database,
    create_student,
    create_students_bulk,
    read_students,
    update_student,
    delete_student,
    delete_all_students,
    search_students_by_name,
    list_students_by_grade,
    show_student_by_id,
    count_total_students
)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        clear()
        print("==== Student Management CLI Application ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Students by Name")
        print("6. List Students by Grade")
        print("7. Show Student Details by ID")
        print("8. Count Total Students")
        print("9. Bulk Insert Students")
        print("10. Delete All Students (DANGEROUS!)")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            create_student(name, age, grade)
            input("Student added! Press Enter to continue...")

        elif choice == '2':
            students = read_students()
            print("\nID | Name           | Age | Grade")
            print("------------------------------------")
            for s in students:
                print(f"{s[0]:<3} | {s[1]:<15} | {s[2]:<3} | {s[3]}")
            input("\nPress Enter to continue...")

        elif choice == '3':
            sid = int(input("Enter student ID: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            grade = input("Enter new grade: ")
            update_student(sid, name, age, grade)
            input("Student updated! Press Enter to continue...")

        elif choice == '4':
            sid = int(input("Enter student ID: "))
            delete_student(sid)
            input("Student deleted! Press Enter to continue...")

        elif choice == '5':
            name = input("Enter name to search: ")
            students = search_students_by_name(name)
            print("\nID | Name           | Age | Grade")
            print("------------------------------------")
            for s in students:
                print(f"{s[0]:<3} | {s[1]:<15} | {s[2]:<3} | {s[3]}")
            input("\nPress Enter to continue...")

        elif choice == '6':
            grade = input("Enter grade to filter: ")
            students = list_students_by_grade(grade)
            print("\nID | Name           | Age | Grade")
            print("------------------------------------")
            for s in students:
                print(f"{s[0]:<3} | {s[1]:<15} | {s[2]:<3} | {s[3]}")
            input("\nPress Enter to continue...")

        elif choice == '7':
            sid = int(input("Enter student ID: "))
            student = show_student_by_id(sid)
            if student:
                print("\nID: {}\nName: {}\nAge: {}\nGrade: {}".format(student[0], student[1], student[2], student[3]))
            else:
                print("Student not found.")
            input("\nPress Enter to continue...")

        elif choice == '8':
            count = count_total_students()
            print(f"\nTotal students: {count}")
            input("\nPress Enter to continue...")

        elif choice == '9':
            n = int(input("How many students do you want to add? "))
            bulk_list = []
            for i in range(n):
                print(f"Student {i+1}:")
                name = input("  Name: ")
                age = int(input("  Age: "))
                grade = input("  Grade: ")
                bulk_list.append((name, age, grade))
            create_students_bulk(bulk_list)
            input(f"{n} students added! Press Enter to continue...")

        elif choice == '10':
            confirm = input("Are you sure? This will delete ALL students! (yes/no): ")
            if confirm.lower() == 'yes':
                delete_all_students()
                input("All students deleted! Press Enter to continue...")
            else:
                input("Operation cancelled. Press Enter to continue...")

        elif choice == '0':
            print("Exiting...")
            break
        else:
            input("Invalid choice! Press Enter...")

if __name__ == "__main__":
    initialize_database()
    menu()

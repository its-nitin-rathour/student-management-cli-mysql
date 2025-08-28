# Student Management CLI (Python + MySQL)

A robust, modular command-line Student Management System built with Python and MySQL. This project enables seamless management of student records through comprehensive CRUD operations, bulk insertion and deletion, advanced search and filtering, user-friendly CSV import/export, and automated reporting features. The codebase is cleanly organized into separate modules for database logic and the application interface.

---

## 🚀 Features

- Add, view, update, and delete students (CRUD)
- Bulk insert and delete students
- Search students by name (partial match)
- Filter students by grade
- View student details by ID
- Count total students
- Export all students to CSV
- Import students from CSV
- Generate reports (students per grade)
- Modular code: separate database and CLI logic
- Easy-to-use terminal menu

---

## 🛠️ Requirements

- Python 3.x
- MySQL Server (running locally or remotely)
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
    - Install via pip:
      ```bash
      pip install mysql-connector-python
      ```

---

## ⚙️ Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/student-management-cli-mysql.git
    cd student-management-cli-mysql
    ```

2. **Install dependencies:**
    ```bash
    pip install mysql-connector-python
    ```

3. **Configure Database Credentials:**
    - Edit `db_code.py` and set your MySQL username and password as needed.

4. **Start MySQL Server:**
    - Ensure your MySQL server is running (locally or on your network).

---

## ▶️ Usage

Start the application by running:

```bash
python app.py
```

You’ll see a menu-driven CLI for managing student records.
Use the interactive menu to add, view, update, delete, search, import/export, and generate reports.

## ▶️ Usage

You’ll see a menu-driven CLI for managing student records.  
Use the interactive menu to add, view, update, delete, search, import/export, and generate reports.

---

## 📦 Import/Export CSV

### Export

- Use the menu to export all student records to a CSV file (default: `students_export.csv`).

### Import

- Prepare a CSV file with the following columns: `Name,Age,Grade`
- Use the menu to import student data from your CSV file (default: `students_import.csv`).

#### **Example CSV (`students_import.csv`):**

```csv
Name,Age,Grade
Alice,21,A
Bob,22,B
Charlie,23,A
```

## 📊 Reports

Generate summary reports such as the number of students per grade. Example output:

```markdown
Grade | Count
--------------
A     | 2
B     | 1
```

## 🧩 Project Structure

```plaintext
student-management-cli-mysql/
│
├── app.py                # Main CLI app interface
├── db_code.py            # Database logic and helper functions
├── README.md
├── students_export.csv   # Example output file after export
└── students_import.csv   # Example input file for import

```

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributions

Pull requests, issues, and feature suggestions are welcome!  
Feel free to fork the repo and submit your improvements.

---

## 🔗 Author

**Nitin Rathour**  
[Email](mailto:nitinrathour_24dsc14@dtu.ac.in)

---

## 💡 Repository Information

- **Repository Name:** `student-management-cli-mysql`
- **Description:**  
  A modular command-line student management system in Python with a MySQL backend. Supports advanced CRUD operations, bulk actions, CSV import/export, search, and reporting.

---


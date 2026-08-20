Python MySQL Database CRUD

A beginner-friendly Python + MySQL command-line project for practicing database and CRUD operations using mysql.connector.

Features

Create a MySQL database

Create a student table

Insert student records

Display table records

Display table structure

Remove a table

Interactive command-line menu

Basic MySQL error handling

Automatic handling of missing table columns in the current table setup

Technologies Used

Python 3

MySQL

mysql-connector-python

Git & GitHub

Project Structure

Python-MySQL-Database-CRUD/
│
├── index.py
├── a.py
└── README.md

Database Structure

The student table uses the following columns:

Column

Data Type

Description

Name

VARCHAR(255)

Student name

Branch

VARCHAR(100)

Student branch/course

Age

INT

Student age

Roll_no

VARCHAR(30)

Student roll number

Roll_no is stored as VARCHAR so that roll numbers containing both letters and numbers can be stored, for example:

23040DBCA0014018

Installation

1. Clone the repository

git clone https://github.com/yashbhawsar2004/Python-MySQL-Database-CRUD.git
cd Python-MySQL-Database-CRUD

2. Install the MySQL connector

pip install mysql-connector-python

3. Make sure MySQL is running

Start your local MySQL server before running the program.

4. Configure your MySQL credentials

In index.py, update the connection details:

database = conn.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD"
)

Do not upload your real MySQL password to GitHub.

Run the Project

python index.py

You will see a menu similar to:

1: Create Database
2: Create Table
3: Insert Data
4: Show Table
5: Describe Table
6: Remove Table
7: Exit

Example

Create a database:

Enter your choice: 1
Enter the name of database you want to create: yash
Database created successfully!

Create a table:

Enter your choice: 2
Enter the database name: yash
Enter the name of table you want to create: hobby
Table created successfully!

Insert a record:

Enter your choice: 3
Enter the database name: yash
Enter the table name: hobby
Enter student name: Vishal
Enter branch: BCA+MCA
Enter age: 22
Enter roll number: 23040DBCA0014018
Data inserted successfully!

Show records:

Enter your choice: 4
Enter the database name: yash
Enter the table name: hobby

('Vishal', 'BCA+MCA', 22, '23040DBCA0014018')

Learning Objectives

This project was created to practice:

Connecting Python with MySQL

Creating databases and tables

Writing SQL queries from Python

Using cursor.execute()

Inserting parameterized values using %s

Fetching records with fetchall()

Using commit() for data-changing operations

Basic exception handling

Git and GitHub workflow

Future Improvements

Planned improvements for the project:

Update student records

Delete individual student records

Search students by roll number or name

Add input validation

Use environment variables for database credentials

Add a graphical user interface

Improve database and table name validation

Author

Yash Bhawsar

GitHub: yashbhawsar2004

License

This project is created for learning and practice purposes.
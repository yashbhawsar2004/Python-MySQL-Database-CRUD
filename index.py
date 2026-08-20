# # import mysql.connector as connector

# # database=connector.connect(
# #     host="localhost",
# #     user="root",
# #     passwd="Yash@123"
# # )

# # cursor=database.cursor()
# # cursor.execute("CREATE DATABASE colleage")
# # print("databse created successfully!")
# # cursor.close()

# # import mysql.connector as con

# # def createtable():
# #     database = con.connect(
# #         host="localhost",
# #         user="root",
# #         passwd="Yash@123",
# #         database="colleage"
# #     )
# #     cursor = database.cursor()

# #     tablename = """CREATE TABLE IF NOT EXISTS student(
# #         Name VARCHAR(225),
# #         roll_no INT,
# #         Age INT
# #     );
# #     """
# #     cursor.execute(tablename)
# #     database.commit()
# #     print("table is created!")

# #     cursor.close()
# #     database.close()

# # createtable()


# # import mysql.connector as conn

# # database = conn.connect(
# #     user="root",
# #     host="localhost",
# #     passwd="Yash@123",
# #     database="colleage"
# # )

# # cursor = database.cursor()

# # Name=input("Enter ypur name: ")
# # department=input("enter your department in which you study: ")
# # age=int(input("enter thee age: "))

# # query = """
# #     INSERT INTO student(Name, department, Age)
# #     VALUES(%s, %s, %s)
# # """


# # cursor.executemany(query, (Name,department,age))
# # database.commit()

# # print("record inserted successfully!")

# # cursor.close()
# # database.close()


# # import mysql.connector



# import mysql.connector

# connection = mysql.connector.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="Yash@123"
# )

# print("MySQL connection successful!")



# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password",
#     database="college"
# )
# print("Connected successfully!")

# cursor = connection.cursor()
# name = input("Enter student name: ")
# course = input("Enter course: ")
# marks = int(input("Enter marks: "))

# query = """
# INSERT INTO Student (Name, Course, Marks)
# VALUES (%s, %s, %s)
# """

# cursor.execute(query, (name, course, marks))
# connection.commit()
# print("Record inserted successfully.")
# connection.close()

# import mysql.connector as conn

# database= conn.connect(
#     host="localhost",
#     user="root",
#     passwd="Yash@123",
#     database="colleage"
# )
# print("my sql connection successful!")

# cursor=database.cursor()
# quary="SELECT * FROM student"
# cursor.execute(quary)

# for row in cursor.fetchall():
#     print(row)

# database.close()


import mysql.connector as conn
from mysql.connector import Error


try:
    database = conn.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

    print("MySQL connection successful!")

    cursor = database.cursor()

except Error as e:
    print("Connection Error:", e)
    exit()




def Create_database():

    name = input("Enter the name of database you want to create: ").strip()

    if not name:
        print("Database name cannot be empty.")
        return

    try:
        query = f"CREATE DATABASE IF NOT EXISTS `{name}`"
        cursor.execute(query)

        print("Database created successfully!")

    except Error as e:
        print("Error:", e)




def Create_table():

    db_name = input("Enter the database name: ").strip()

    if not db_name:
        print("Database name cannot be empty.")
        return

    try:

        # Select database
        cursor.execute(f"USE `{db_name}`")

        tname = input("Enter the name of table you want to create: ").strip()

        if not tname:
            print("Table name cannot be empty.")
            return

        # Create correct table
        table_query = f"""
        CREATE TABLE IF NOT EXISTS `{tname}` (
            Name VARCHAR(255),
            Branch VARCHAR(100),
            Age INT,
            Roll_no VARCHAR(30)
        )
        """

        cursor.execute(table_query)

        print("Table created successfully!")

        # Check existing columns
        cursor.execute(f"DESCRIBE `{tname}`")

        columns = cursor.fetchall()

        existing_columns = [column[0].lower() for column in columns]

        # Add missing columns if old table exists
        if "branch" not in existing_columns:
            cursor.execute(
                f"ALTER TABLE `{tname}` ADD COLUMN Branch VARCHAR(100)"
            )
            print("Branch column added.")

        if "age" not in existing_columns:
            cursor.execute(
                f"ALTER TABLE `{tname}` ADD COLUMN Age INT"
            )
            print("Age column added.")

        if "roll_no" not in existing_columns:
            cursor.execute(
                f"ALTER TABLE `{tname}` ADD COLUMN Roll_no VARCHAR(30)"
            )
            print("Roll_no column added.")

        database.commit()

    except Error as e:
        print("Error:", e)




def insert_into_table():

    db_name = input("Enter the database name: ").strip()

    if not db_name:
        print("Database name cannot be empty.")
        return

    try:

        # Select database
        cursor.execute(f"USE `{db_name}`")

        tablename = input(
            "Enter the table name in which you want to insert values: "
        ).strip()

        if not tablename:
            print("Table name cannot be empty.")
            return

        # Check whether table exists
        cursor.execute(f"SHOW TABLES LIKE '{tablename}'")

        if cursor.fetchone() is None:
            print("Table does not exist.")
            return

        # Take input
        name = input("Enter student name: ").strip()
        branch = input("Enter branch: ").strip()

        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Age must be a number.")
            return

        # Roll number can contain letters
        roll_no = input("Enter roll number: ").strip()

        # Insert query
        query = f"""
        INSERT INTO `{tablename}`
        (Name, Branch, Age, Roll_no)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, branch, age, roll_no)

        cursor.execute(query, values)

        database.commit()

        print("Data inserted successfully!")

    except Error as e:
        print("Error:", e)


def show_table():

    db_name = input("Enter the database name: ").strip()

    try:

        cursor.execute(f"USE `{db_name}`")

        table_name = input(
            "Enter the table name you want to show: "
        ).strip()

        cursor.execute(f"SELECT * FROM `{table_name}`")

        result = cursor.fetchall()

        if result:

            print("\nStudent Records")
            print("-" * 60)

            for row in result:
                print(row)

        else:
            print("Table is empty.")

    except Error as e:
        print("Error:", e)




def describe_table():

    db_name = input("Enter the database name: ").strip()

    try:

        cursor.execute(f"USE `{db_name}`")

        table_name = input(
            "Enter the table name: "
        ).strip()

        cursor.execute(f"DESCRIBE `{table_name}`")

        result = cursor.fetchall()

        print("\nTable Structure")
        print("-" * 60)

        for row in result:
            print(row)

    except Error as e:
        print("Error:", e)




def Remove_table():

    db_name = input("Enter the database name: ").strip()

    try:

        cursor.execute(f"USE `{db_name}`")

        tablename = input(
            "Enter the name of table you want to drop: "
        ).strip()

        query = f"DROP TABLE IF EXISTS `{tablename}`"

        cursor.execute(query)

        database.commit()

        print("Table removed successfully!")

    except Error as e:
        print("Error:", e)




while True:

    print("""
=============================
       MYSQL MENU
=============================

1: Create Database
2: Create Table
3: Insert Data
4: Show Table
5: Describe Table
6: Remove Table
7: Exit
""")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        Create_database()

    elif choice == "2":
        Create_table()

    elif choice == "3":
        insert_into_table()

    elif choice == "4":
        show_table()

    elif choice == "5":
        describe_table()

    elif choice == "6":
        Remove_table()

    elif choice == "7":
        print("Thank you for using the program.")
        break

    else:
        print("Invalid choice. Please enter 1-7.")



cursor.close()
database.close()

print("MySQL connection closed.")
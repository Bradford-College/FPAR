"""
I will only use builin modules for this project
No external libraries will be used so there is no need to install dependencies
As long as you have a standard python installation on windows,
everything should run smoothly.
"""
import sqlite3
import os
import builtins
from contextlib import closing
from Tasks.addStudent import addStudent
from Tasks.deleteStudent import deleteStudent
from Tasks.getStudent import getStudent
from mygui import pygui as gui
import mymisc.startup as mm
"""
Yes I know this is a horribly hacky way to
get a global variable I can use within the imported modules
No I don't care
"""
builtins.DB_PATH = 'Student_Records'
builtins.DB_NAME = 'student_records.db'
builtins.DB_FILE = DB_PATH + "/" + DB_NAME

#
# def startup():
#     """
#     startup - check if the database exists
#     if not create it and initialize the table
#     This function will be called at the start of the program
# """
#     if not os.path.exists(DB_PATH):
#         os.makedirs(DB_PATH)
#     if not initialize_db():
#         print("Error initializing database.")
#         exit(1)
#
#
# def initialize_db() -> bool:
#     try:
#         with closing(sqlite3.connect(DB_FILE)) as conn:
#             with closing(conn.cursor()) as cursor:
#                 _ = cursor.execute('''
#                     CREATE TABLE IF NOT EXISTS students (
#                         student_number INTEGER PRIMARY KEY,
#                         student_name TEXT NOT NULL,
#                         course_name TEXT NOT NULL
#                     )
#                 ''')
#                 conn.commit()
#                 print("Database initialized successfully.")
#     except sqlite3.Error as e:
#         print("Encountered error initializing db: ", e)
#         return False
#     return True
#


def test_addStudent():
    student_detail = {
        'student_name': 'John Doe',
        'student_number': '123456',
        'course_name': 'Computer Science'
    }
    student_detail2 = {
        'student_name': 'Jane Doe',
        'student_number': '654321',
        'course_name': 'Computer Science'
    }
    print("Adding students to the database...")
    try:
        addStudent(student_detail)
        addStudent(student_detail2)
    except Exception as e:
        print("An error occurred while adding students:", e)
        raise e


def test_deleteStudent():
    student_number = '123456'
    fake_student_number = '696969'
    invalid_student_number = 'lemon'
    try:
        print("Deleting valid student from the database...")
        deleted_student = deleteStudent(student_number)
        print(
            f"Student {deleted_student['student_name']} deleted successfully.")
    except Exception as e:
        print("An error occurred while deleting student:", e)
        raise e
    try:
        print("Deleting fake student from the database...")
        print(deleteStudent(fake_student_number))
    except Exception as e:
        print("An error occurred while deleting student:", e)
    try:
        print("Deleting invalid student from the database...")
        print(deleteStudent(invalid_student_number))
    except Exception as e:
        print("An error occurred while deleting student:", e)


def test_getStudent():
    student_number = '123456'
    invalid_student_number = "lemon"
    fake_student_number = '696969'
    try:
        print("Retrieving student from the database...")
        student_detail = getStudent(student_number)
        print(f"Student found: {student_detail}")
    except Exception as e:
        print("An error occurred while retrieving student:", e)
        raise e
    try:
        print("Retrieving fake student from the database...")
        print(getStudent(fake_student_number))
    except Exception as e:
        print("An error occurred while retrieving student:", e)
    try:
        print("Retrieving invalid student from the database...")
        print(getStudent(invalid_student_number))
    except Exception as e:
        print("An error occurred while retrieving student:", e)


def main():
    mm.startup()
    print("Welcome to the student records database!")
    test_addStudent()
    test_getStudent()
    test_deleteStudent()
    print("Thank you for using the student records database.")
    _ = gui.messagebox(
        "Thank you for using the student records database.",
        "Goodbye!")


if __name__ == '__main__':
    main()

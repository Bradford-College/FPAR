'''
Import and test your functions here
Example:
    - from Tasks.addStudent import addStudent

Use this section to test your functions and verify if the output is as expected.
Using assert or unittest would fetch you more marks.
'''

'''
Test your functions here
'''


import sqlite3
import os
import builtins
from contextlib import closing
from Tasks.addStudent import addStudent
from Tasks.deleteStudent import deleteStudent
from Tasks.getStudent import getStudent
DB_PATH = 'Test_Student_Records'
DB_NAME = 'Test_student_records.db'
DB_FILE = DB_PATH + "/" + DB_NAME


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


if __name__ == "__main__":
    test_addStudent()
    test_getStudent()
    test_deleteStudent()

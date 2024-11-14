"""
I will only use builin modules for this project
No external libraries will be used so there is no need to install dependencies
As long as you have a standard python installation on windows,
everything should run smoothly.
"""
import sqlite3
import os
from datetime import datetime

# global variables
# database file name
DB_PATH = 'Student_Records'
DB_NAME = 'student_records.db'
DB_FILE = DB_PATH + "/" + DB_NAME
# startup - check if the database exists
# if not create it and initialize the table


def startup():
    # The database file is stored in the directory student_records
    # It is named student_records.db
    if not os.path.exists('Student_Records'):
        os.makedirs('Student_Records')
    if not initialize_db():
        print("Error initializing database.")
        exit(1)


def initialize_db() -> bool:
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        _ = cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_number INTEGER PRIMARY KEY,
                student_name TEXT NOT NULL,
                course_name TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print("Encountered error: ", e)
        return False
    return True


def getStudent(student_num: str) -> dict[str, str]:
    '''
    Description: This function searches the database for a student using the student_number argument.

    Args:
        student_number (str): The number of the student (string, converted to integer).

    Returns:
        student_detail (dict): A dictionary containing the following key-value pairs:
            - 'student_name': The name of the student.
            - 'student_number': The student number.
            - 'course_name': The name of the course.

    Conditions:
        The use of error handling routine is compulsory.
    '''
    try:
        # Ensure student_number is an integer
        student_number = int(student_num)
    except ValueError as e:
        print("Error: Student number must be a numeric value.")
        raise e
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        _ = cursor.execute(
            'SELECT * FROM students WHERE student_number = ?',
            (student_number,))
        row = cursor.fetchone()

        if row:
            student_detail = {
                'student_number': row[0],
                'student_name': row[1],
                'course_name': row[2]
            }
            return student_detail
        else:
            raise Exception(f"No student found with number {student_number}")
    except sqlite3.Error as e:
        print(f"An error occurred while retrieving the student: {e}")
        raise e
    finally:
        try:
            conn.close()
        except NameError:
            pass


def addStudent(student_detail: dict[str, str]) -> None:
    '''
    Description: This function accepts students' details and writes to the database.
    Args:
        student_detail (dict): A dictionary containing the following key-value pairs:
            - 'student_name': The name of the student.
            - 'student_number': The student number (string, converted to integer).
            - 'course_name': The name of the course.

    Returns:
        None. Prints a statement confirming that the record was written.

    Conditions:
        The use of error handling routine is compulsory.
    '''
    try:
        # Ensure student_number is an integer
        student_number = int(student_detail['student_number'])
    except ValueError as e:
        print("Error: Student number must be a numeric value.")
        raise e
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        _ = cursor.execute('''
            INSERT INTO students (student_number, student_name, course_name)
            VALUES (?, ?, ?)
        ''', (student_number, student_detail['student_name'], student_detail['course_name']))
        conn.commit()
        print(f"Student {student_detail['student_name']} added successfully.")
    except sqlite3.IntegrityError:
        print("Student number already exists!")
    except sqlite3.Error as e:
        print("An error occurred while adding the student:", e)
    finally:
        try:
            conn.close()
        except NameError:
            pass


def deleteStudent(student_number: str) -> dict[str, str]:
    """
    Deletes a student record 

    Parameters:
        student_number (str): The unique identifier for the student.

    Returns:
        dict: A dictionary containing details of the deleted student, including:
            - 'student_name': Name of the student.
            - 'student_number': The student's unique identifier.
            - 'course_name': The student's course name.

    Note:
        This function requires the implementation of error handling.
    """
    # Ensure student_number is an integer
    try:
        student_id = int(student_number)
    except ValueError as e:
        print("Error: Student number must be a numeric value.")
        raise e
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        _ = cursor.execute(
            'SELECT * FROM students WHERE student_number = ?', (student_id,))
        row = cursor.fetchone()
        if not row:
            raise Exception(f"No student found with number {student_number}")
        student_detail = {
            'student_number': row[0],
            'student_name': row[1],
            'course_name': row[2]
        }
        _ = cursor.execute(
            'DELETE FROM students WHERE student_number = ?', (student_id,))
        conn.commit()
        return student_detail
    except sqlite3.Error as e:
        print("An error occurred while deleting the student:", e)
        raise e
    finally:
        conn.close()


def test_addStudent():
    student_detail = {
        'student_name': 'John Doe',
        'student_number': '123456',
        'course_name': 'Computer Science'
    }
    addStudent(student_detail)


def test_deleteStudent():
    student_number = '123456'
    fake_student_number = '696969'
    print(deleteStudent(student_number))
    print(deleteStudent(fake_student_number))


def test_getStudent():
    student_number = "lemon"
    fake_student_number = '696969'
    print(getStudent(student_number))
#    print(getStudent(fake_student_number))


def main():
    startup()
    print("Welcome to the student records diatabase!")
    test_deleteStudent()


if __name__ == '__main__':
    main()

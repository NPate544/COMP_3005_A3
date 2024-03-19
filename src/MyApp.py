import psycopg2
from psycopg2 import sql

# Database connection parameters
conn_params = {
    "database": "Assignment_3",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

def db_connect(func):
    """Decorator for database connection and cleanup."""
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(**conn_params)
        try:
            print(f"\nExecuting {func.__name__}...")
            result = func(conn, *args, **kwargs)
            conn.commit()
            print(f"Completed {func.__name__}.\n")
            return result
        except Exception as e:
            conn.rollback()
            print(f"Database error: {e}")
        finally:
            conn.close()
    return wrapper

@db_connect
def getAllStudents(conn):
    print("Retrieving all students...")
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students;")
        students = cur.fetchall()
        if not students:
            print("No students found.\n")
            return
        for row in students:
            row = list(row)  # Convert tuple to list to be able to modify it
            row[4] = row[4].strftime('%Y-%m-%d')  # Format the date
            print(tuple(row))  
        print() 

@db_connect
def addStudent(conn, first_name, last_name, email, enrollment_date):
    print(f"Adding student: {first_name} {last_name}")
    with conn.cursor() as cur:
        cur.execute(sql.SQL("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"),
                    (first_name, last_name, email, enrollment_date))
    print("Student added.\n")

@db_connect
def updateStudentEmail(conn, student_id, new_email):
    print(f"Updating email for student ID {student_id}")
    with conn.cursor() as cur:
        cur.execute(sql.SQL("UPDATE students SET email = %s WHERE student_id = %s;"),
                    (new_email, student_id))
    print("Email updated.\n")

@db_connect
def deleteStudent(conn, student_id):
    print(f"Deleting student ID {student_id}")
    with conn.cursor() as cur:
        cur.execute(sql.SQL("DELETE FROM students WHERE student_id = %s;"),
                    (student_id,))
    print("Student deleted.\n")

@db_connect
def checkStudentExists(conn, student_id):
    """Check if a student exists by ID."""
    with conn.cursor() as cur:
        cur.execute("SELECT EXISTS(SELECT 1 FROM students WHERE student_id = %s);", (student_id,))
        exists = cur.fetchone()[0]
        return exists

def main_menu():
    print("1. Retrieve all students")
    print("2. Add a new student")
    print("3. Update a student's email")
    print("4. Delete a student")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            getAllStudents()
        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == "3":
            while True:
                student_id = input("Enter student ID to update email: ")
                if not checkStudentExists(student_id):
                    print("Student ID does not exist. Try again!")
                    continue
                new_email = input("Enter new email: ")
                updateStudentEmail(student_id, new_email)
                break
        elif choice == "4":
            while True:
                student_id = input("Enter student ID to delete: ")
                if not checkStudentExists(student_id):
                    print("Student ID does not exist. Try again!")
                    continue
                deleteStudent(student_id)
                break
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
if __name__ == "__main__":
    print("Starting the database operations...\n")
    main()
    print("\nDatabase operations completed.")

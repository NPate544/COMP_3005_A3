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
def resetDatabase(conn):
    """Reset the students table and insert default data."""
    with conn.cursor() as cur:
        # Delete all existing records
        print("Deleting all existing students...")
        cur.execute("DELETE FROM students;")
        
        # Insert default data
        print("Inserting default data...")
        default_students = [
            ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
            ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
            ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
        ]
        cur.executemany(sql.SQL("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"), default_students)
    print("Database reset to default.\n")

# Example usage
if __name__ == "__main__":
    print("Starting the database reset operation...\n")
    resetDatabase()
    print("\nDatabase operations completed.")
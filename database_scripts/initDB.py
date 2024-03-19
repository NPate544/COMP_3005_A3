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
def init_db(conn):
    """Initialize the database schema."""
    print("Initializing database schema...")
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id SERIAL PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                enrollment_date DATE
            );
        """)
    print("Database schema initialized.\n")

@db_connect
def seed_db(conn):
    """Seed the database with initial data."""
    print("Seeding the database with initial data...")
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
            ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
            ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
            ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
            ON CONFLICT (email) DO NOTHING;
        """)
    print("Database seeded with initial data.\n")


if __name__ == "__main__":
    print("Starting the database operations...\n")
    init_db()
    seed_db()
    print("\nDatabase operations completed.")
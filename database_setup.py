import sqlite3

def setup_database():
    conn = sqlite3.connect("student_data.db")
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Create attendance table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    """)

    # Create result table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            subject TEXT NOT NULL,
            marks INTEGER NOT NULL,
            grade TEXT NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    """)

    conn.commit()
    conn.close()
    print("Database setup completed successfully.")

if __name__ == "__main__":
    setup_database()

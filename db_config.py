import sqlite3


def create_tables():
    conn = sqlite3.connect("banking_system.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        account_number TEXT UNIQUE NOT NULL,
        dob TEXT NOT NULL,
        city TEXT,
        password TEXT NOT NULL,
        balance REAL DEFAULT 2000,
        contact TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        address TEXT,
        status TEXT DEFAULT 'active'
    )
    """)

    # Transactions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_number TEXT NOT NULL,
        type TEXT NOT NULL,
        amount REAL NOT NULL,
        date_time TEXT DEFAULT CURRENT_TIMESTAMP,
        details TEXT,
        FOREIGN KEY (account_number) REFERENCES users (account_number)
    )
    """)

    conn.commit()
    conn.close()


def get_connection():
    return sqlite3.connect("banking_system.db")


# Initialize database
create_tables()

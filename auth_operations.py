import bcrypt
from db_config import get_connection


def login():
    conn = get_connection()
    cursor = conn.cursor()

    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")

    cursor.execute(
        "SELECT * FROM users WHERE account_number = ?", (account_number,))
    user = cursor.fetchone()

    if not user:
        print("Account not found.")
        conn.close()
        return None

    # Ensure that both the stored password and the input password are in byte format for comparison
    # Get the stored password from the database (this should be a hashed password in bytes)
    stored_password = user[4]

    if bcrypt.checkpw(password.encode('utf-8'), stored_password):
        print(f"Welcome, {user[1]}!")
        conn.close()
        return user
    else:
        print("Invalid password.")
        conn.close()
        return None

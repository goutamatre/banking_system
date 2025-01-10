import bcrypt
from db_config import get_connection
from validations import validate_name, validate_contact, validate_email, validate_password
import random


def add_user():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Enter your name: ")
    if not validate_name(name):
        print("Invalid name.")
        return

    dob = input("Enter your DOB (YYYY-MM-DD): ")
    city = input("Enter your city: ")

    password = input("Enter a strong password: ")
    if not validate_password(password):
        print("Password must contain at least 8 characters, including an uppercase letter, a lowercase letter, a number, and a special character.")
        return

    # Hash the password properly using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    initial_balance = float(input("Enter initial balance (minimum ₹2000): "))
    if initial_balance < 2000:
        print("Initial balance must be at least ₹2000.")
        return

    contact = input("Enter your contact number: ")
    if not validate_contact(contact):
        print("Invalid contact number.")
        return

    email = input("Enter your email: ")
    if not validate_email(email):
        print("Invalid email.")
        return

    address = input("Enter your address: ")

    account_number = str(random.randint(1000000000, 9999999999))

    try:
        cursor.execute("""
        INSERT INTO users (name, account_number, dob, city, password, balance, contact, email, address)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, account_number, dob, city, hashed_password, initial_balance, contact, email, address))
        conn.commit()
        print(f"User created successfully! Account Number: {account_number}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

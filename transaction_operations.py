from db_config import get_connection
from datetime import datetime


def show_balance(user):
    print(f"Current Balance: ₹{user[5]}")


def credit_amount(user):
    conn = get_connection()
    cursor = conn.cursor()

    amount = float(input("Enter amount to credit: "))
    new_balance = user[5] + amount

    cursor.execute(
        "UPDATE users SET balance = ? WHERE account_number = ?", (new_balance, user[2]))
    cursor.execute("""
    INSERT INTO transactions (account_number, type, amount, date_time)
    VALUES (?, 'credit', ?, ?)
    """, (user[2], amount, datetime.now()))
    conn.commit()

    print(f"₹{amount} credited. New Balance: ₹{new_balance}")
    conn.close()


def debit_amount(user):
    conn = get_connection()
    cursor = conn.cursor()

    amount = float(input("Enter amount to debit: "))
    if user[5] < amount:
        print("Insufficient balance.")
        conn.close()
        return

    new_balance = user[5] - amount

    cursor.execute(
        "UPDATE users SET balance = ? WHERE account_number = ?", (new_balance, user[2]))
    cursor.execute("""
    INSERT INTO transactions (account_number, type, amount, date_time)
    VALUES (?, 'debit', ?, ?)
    """, (user[2], amount, datetime.now()))
    conn.commit()

    print(f"₹{amount} debited. New Balance: ₹{new_balance}")
    conn.close()

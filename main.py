from user_operations import add_user
from auth_operations import login
from transaction_operations import show_balance, credit_amount, debit_amount


def main_menu():
    while True:
        print("\nBANKING SYSTEM")
        print("1. Add User")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            user = login()
            if user:
                user_menu(user)
        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice.")


def user_menu(user):
    while True:
        print("\nUSER MENU")
        print("1. Show Balance")
        print("2. Credit Amount")
        print("3. Debit Amount")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_balance(user)
        elif choice == "2":
            credit_amount(user)
        elif choice == "3":
            debit_amount(user)
        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()

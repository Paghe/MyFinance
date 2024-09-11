from account.user_class import User
from account.tracker_class import Tracker
from utils.utils import save_to_csv


def tracker_menu(user):
    print(f"Your expenses amount {user.get_total_expenses()}")
    while True:
        try:
            key = input("Please add a category: ")
            if key.lower() == "exit":
                print("\nExiting from expenses... back to menu")
                break
            value = input("Please add your new expense: ")
            if value.lower() == "exit":
                print("\nExiting from expenses... back to menu")
                break
            if value and key:
                if not value.isalpha():
                    user.add_expenses(key.lower(), float(value))
                else:
                    print("Invalid value for expense")
        except KeyboardInterrupt:
            print("\nProcess interrupted by user. Exiting...")
            break
        except EOFError:
            print("\nProcess interrupted by user. Exiting...")
            break
                 
                 
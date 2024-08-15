from account.user_class import User
from account.tracker_class import Tracker
from utils.utils import save_to_csv



def tracker_menu(user):
    print(f"Your expenses amount {user.get_total_expenses()}")
    while True:
        try:
            value = input("Please add your new expense: ")
            if value:
                key = input("Please add a category: ")
            if value and key:
                user.add_expenses(key.lower(), float(value))
        except KeyboardInterrupt:
            print("\nProcess interrupted by user. Exiting...")
            break
                 
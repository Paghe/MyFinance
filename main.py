from account.user_class import User
from utils.utils import insert_data, save_to_csv, file_data
from utils.reader import read_from_csv
from utils.menu import run_menu

import os
def run_account():
    if file_data():
        attributes, expenses = read_from_csv()
        account = User(attributes)
        for category, amount in expenses.items():
            account.add_expenses(category, amount)
    else:  
        attributes = insert_data()
        account = User(attributes)
        if account:
            account.insert_account_balance()
            save_to_csv(account)
    run_menu(account)

def main():
    run_account()
   
if __name__ == "__main__":
    main()
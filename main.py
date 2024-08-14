from account.user_class import User
from utils.utils import insert_data, save_to_csv, file_data
from utils.reader import read_from_csv
import os
def run_account():
    if file_data():
        attributes = read_from_csv()
        account = User(attributes)
    else:  
        attributes = insert_data()
        account = User(attributes)
        if account:
            account.insert_account_balance()
            save_to_csv(attributes)
    
def main():
    run_account()
   
if __name__ == "__main__":
    main()
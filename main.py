from user_class import User
from utils import insert_data, save_to_csv

def run_account():
    attributes = insert_data()
    account = User(attributes)
    if account:
        account.insert_account_balance()
        save_to_csv(attributes)
    
def main():
    run_account()
   
if __name__ == "__main__":
    main()
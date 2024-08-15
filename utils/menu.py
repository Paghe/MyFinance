from account.user_class import User
from account.tracker_class import Tracker
from utils.utils import save_to_csv
from utils.tracker import tracker_menu

def print_detail_user(user, command):
    if (command == '1'):
        print()
        for key, value in user.get_attribute().items():
            print(f"{key.capitalize()}: {value}")
        print()

def shutdown_app(user, command):
    if command == '7' or command.lower() == 'exit':
        print(f"\nGood Bye {user.get_attribute_value('name')}!")
        return True
    return False
        
def update_Name(user, command):
    if command == '2':
        flag = False
        while not flag:
            value = input('Please add your new name: ')
            if value.isalpha():
                user.set_attribute('name', value)
                flag = True
                
def update_Age(user, command):
    if command == '3':
        flag = False
        while not flag:
            value = input('Please add your new age: ')
            if value:
                user.set_attribute('age', int(value))
                flag = True
                
def update_Income(user, command):
    if command == '4':
        flag = False
        while not flag:
            value = input('Please add your new income: ')
            if value:
                user.set_attribute('income', float(value))
                flag = True
                
def update_Balance(user, command):
    if command == '4':
        flag = False
        while not flag:
            value = input('Please add your new Balance: ')
            if value:
                user.set_attribute('owning', float(value))
                flag = True
def expenses(user, command):
    if command == '6':
        tracker_menu(user)
          
def user_command(user, command):
    print_detail_user(user, command)
    update_Name(user, command)
    update_Age(user, command)
    update_Income(user, command)
    update_Balance(user, command)
    expenses(user, command)

def run_menu(user):
    print("\n------ USER MENU ------")
    print(f"Hello {user.get_attribute_value('name')}!")
    list_menu = ["1. View User Details", "2. Update Name","3. Update Age",
                 "4. Update Income","5. Update Balance", "6. Update your expenses", "7. EXIT"]
    for x in range(len(list_menu)):
        print(list_menu[x])
    while True:
        try:
            command = input("Choose an option: ")
            if shutdown_app(user, command):
                break
            user_command(user, command)
        except KeyboardInterrupt:
               print("\nProcess interrupted by user. Exiting...")
               break
    save_to_csv(user)
    
   

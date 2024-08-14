from account.user_class import User

def print_detail_user(user, command):
    if (command == '1'):
        print()
        for key, value in user.items():
            print(f"{key.capitalize()}: {value}")
        print()

def shutdown_app(user, command):
    if command == '6' or command.lower() == 'exit':
        print(f"\nGood Bye {user['name']}!")
        exit()
          
def user_command(user, command):
    print_detail_user(user, command)
    shutdown_app(user, command)

def run_menu(user):
    print("\n------ USER MENU ------")
    print(f"Hello {user['name']}!")
    list_menu = ["1. View User Details", "2. Update Name","3. Update Age",
                 "4. Update Income","5. Update Balance", "6. EXIT"]
    for x in range(len(list_menu)):
        print(list_menu[x])
    while True:
        try:
            command = input("Choose an option: ")
            user_command(user, command)
        except KeyboardInterrupt:
               print("\nProcess interrupted by user. Exiting...")
               break
    
   

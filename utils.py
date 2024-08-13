from user_class import User


def insert_data():
    store = {}
    flag = 0
    key_value = ["name", "lastname", "age", "income"]
    print("please fill the data required:\n")
    try:
        while True and not flag:
            for key in key_value:
                tmp = input(f"your {key}: ")
                if not tmp:
                    print("Invalid Input!")
                store[key] = tmp
                if len(store) >= 3:
                    flag = 1
                    break
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
    return store
import csv

def check_value(token, value):
    if ((token == "name"  or token == "lastname") and value.isalpha()):
        return value
    elif token == "age" or token == 'income':
        try:
            num = float(value) if token == 'income' else int(value)
            return num
        except ValueError:
            print("Invalid number format.")
            return -1
    else:
        return -1
    
def insert_data():
    store = {}
    key_value = ["name", "lastname", "age", "income"]
    print("please fill the data required:\n")
    try:
        while len(store) <= 3:
            for key in key_value:
                if key in store:
                    continue
                tmp = input(f"your {key}: ")
                if check_value(key, tmp) == -1:
                    print("Invalid Input!")
                    continue
                store[key] = tmp
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
    return store

def save_to_csv(attributes, filename='user_data.csv'):
    fieldnames = attributes.keys()
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader
        writer.writerow(attributes)
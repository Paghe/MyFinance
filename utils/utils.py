import csv
from datetime import datetime
from pathlib import Path
import os

def check_value(token, value):
    if ((token == "name" or token == "lastname") and value.isalpha()):
        return value
    elif (token == "date"):
        return value
    elif token == "age" or token == 'income' or token == 'owning':
        try:
            num = float(value) if token == 'income' or token == 'owning' else int(value)
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

def save_to_csv(user, filename='user_data.csv'):
    current_date = datetime.now().strftime('%d-%m-%Y')
    user.set_attribute('date', current_date) 
    attributes = user.get_attribute()
    expenses = user.get_expenses()
    row_expenses = [f"{key.upper()}: {value}" for key, value in expenses.items()]
    user_rows = [f"{key.upper()}: {value}" for key, value in attributes.items()]
    all_rows = user_rows + row_expenses
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in all_rows:
            writer.writerow([row])

def file_data():
    file = Path('user_data.csv')
    if file.exists():
        return 1
    else:
        return 0
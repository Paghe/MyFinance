import csv
from datetime import datetime
from pathlib import Path
import os

def check_value(token, value):
    if ((token == "name"  or token == "lastname") and value.isalpha()):
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

def save_to_csv(attributes, filename='user_data.csv'):
    current_date = datetime.now().strftime('%d-%m-%Y')
    rows = [f"DATE: {current_date}"] + [f"{key.upper()}: {value}" for key, value in attributes.items()]
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow([row])
        writer.writerow([])

def file_data():
    file = Path('user_data.csv')
    if file.exists():
        return 1
    else:
        return 0
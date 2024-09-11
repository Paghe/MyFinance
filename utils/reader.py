import csv
import os
from account.user_class import User
from utils.utils import check_value

def split_for_hashmap(row, index):
   
    split = row[0].split(':')[index].strip() if len(row[0].split(":")) > index else None
    if split:
        return(split)
    

def read_from_csv(filename='user_data.csv'):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "../", filename)
    attributes = {}
    expenses = {}
    reading_expenses = False
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                if row[0].strip().lower() == "expenses":
                    reading_expenses = True
                    continue
                if reading_expenses:
                    key = split_for_hashmap(row, 0).lower()
                    value = check_value(key, split_for_hashmap(row, 1))
                    if key and value != -1:
                        expenses[key] = value
                key = split_for_hashmap(row, 0).lower()
                tmp_value = split_for_hashmap(row, 1)
                value = check_value(key, tmp_value)
                if key and value != -1:
                    attributes[key] = value
        return attributes, expenses
    
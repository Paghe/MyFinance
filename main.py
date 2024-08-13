from user_class import User
from utils import insert_data

def main():
    attributes = insert_data()
    test = User(attributes)
    print(test.attributes["name"])
    
if __name__ == "__main__":
    main()
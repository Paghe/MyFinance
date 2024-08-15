from account.tracker_class import Tracker

class User(Tracker):
    def __init__(self, attributes) -> None:
        super().__init__()
        self.attributes = attributes
    
    def __str__(self) -> str:
        return (f"Hello, my name is {self.name} "
                    f"{self.lastname}. I'm {self.age} and I have {self.income}.")
    category = ["food", "rent", "entertainment"]
    # maybe an hashmap where store the total of each category?
    def insert_account_balance(self):
        print("How much money do you have on your banck account?")
        try:
            amount = input("Insert the amount: ")
            self.attributes["owning"] = amount
        except KeyboardInterrupt:
             print("\nProcess interrupted by user. Exiting...")

    def get_attribute(self):
        return self.attributes
    
    def get_attribute_value(self, key):
        if self.attributes[key]:
            return self.attributes[key]
        
    def set_attribute(self, key, value):
        self.attributes[key] = value

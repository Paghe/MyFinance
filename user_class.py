class User:
    def __init__(self, attributes) -> None:
        self.attributes = attributes
    
    def __str__(self) -> str:
        return (f"Hello, my name is {self.name} "
                    f"{self.lastname}. I'm {self.age} and I have {self.income}.")
    
    category = ["food", "rent", "entertainment"]
    # maybe an hashmap where store the total of each category?
    

        
    
        
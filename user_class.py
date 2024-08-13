class User:
    def __init__(self, name, lastname, age) -> None:
        self.name = name
        self.lastname = lastname
        self.age = age
    def __str__(self) -> str:
        return (f"Hello, my name is {self.name} "
                    f"{self.lastname}. I'm {self.age}.")
    
class Tracker:
    def __init__(self) -> None:
        self.expenses = {}
    def add_expenses(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        print(f"added expense: {amount} to {category}")
        print(f"total expense in {category} is {self.expenses[category]}")
    
    def get_total_expenses(self):
        return sum(self.expenses.values())
    
    def get_expenses_by_category(self, category):
        return self.expenses.get(category, 0)
    
    def get_expenses(self):
        return self.expenses
    
    def clear_expenses(self):
        self.expenses.clear()
        print("All expenses cleared")
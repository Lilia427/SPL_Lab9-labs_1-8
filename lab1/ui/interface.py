from services.operations import calculate
from data.history import History
from data.settings import Settings
from services.memory import Memory

class UserInterface:
    def __init__(self):
        self.history = History()
        self.memory = Memory()
        self.settings = Settings()

    def start(self):
        print("Welcome to the Calculator!")
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                operator = input("Enter an operator (+, -, *, /, ^, √, %): ")
                num2 = None
                if operator not in ('√',):
                    num2 = float(input("Enter the second number: "))
                
                result = calculate(num1, operator, num2)
                if result is not None:
                    result = self.settings.round_result(result)
                    print(f"Result: {result}")
                    self.history.add_entry(num1, operator, num2, result)

                    save_memory = input("Do you want to save this result to memory? (y/n): ")
                    if save_memory.lower() == 'y':
                        self.memory.store(result)
                    
                    view_history = input("Do you want to view calculation history? (y/n): ")
                    if view_history.lower() == 'y':
                        self.history.show()
                
                new_calc = input("Would you like to perform another calculation? (y/n): ")
                if new_calc.lower() != 'y':
                    print("Goodbye!")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers correctly.")

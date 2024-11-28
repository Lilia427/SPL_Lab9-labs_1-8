from lab2.data.history import History
from lab2.data.settings import Settings
from lab2.services.operations import Operations
from lab2.services.memory import Memory


class Calculator:
    def __init__(self, decimal_places=2):
        self.operations = Operations()
        self.memory = Memory()
        self.history = History()
        self.settings = Settings(decimal_places=decimal_places)

    def get_user_input(self):
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                operator = input("Enter an operator (+, -, *, /, ^, √, %): ")
                num2 = None
                if operator not in ('√',):
                    num2 = float(input("Enter the second number: "))
                return num1, operator, num2
            except ValueError:
                print("Invalid input. Please enter numbers correctly.")

    def run(self):
        while True:
            num1, operator, num2 = self.get_user_input()
            if not self.operations.validate_operator(operator):
                continue

            result = self.operations.calculate(num1, operator, num2)

            if result is not None:
                result = self.settings.round_result(result)
                print(f"Result: {result}")
                self.history.add_entry(num1, operator, num2, result)

            save_memory = input("Do you want to save this result to memory? (y/n): ")
            if save_memory.lower() == 'y' and result is not None:
                self.memory.store(result)

            view_history = input("View calculation history? (y/n): ")
            if view_history.lower() == 'y':
                self.history.show()

            new_calc = input("Would you like to perform another calculation? (y/n): ")
            if new_calc.lower() != 'y':
                print("Goodbye!")
                break

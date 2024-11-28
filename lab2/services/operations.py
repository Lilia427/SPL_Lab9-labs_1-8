import math

class Operations:
    """Base class for mathematical operations."""
    def validate_operator(self, operator):
        if operator in ('+', '-', '*', '/', '^', '√', '%'):
            return True
        else:
            print("Invalid operator. Please enter one of +, -, *, /, ^, √, %.")
            return False

    def calculate(self, num1, operator, num2):
        try:
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                return num1 / num2
            elif operator == '^':
                return num1 ** num2
            elif operator == '√':
                if num1 < 0:
                    raise ValueError("Cannot calculate square root of a negative number.")
                return math.sqrt(num1)
            elif operator == '%':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot calculate modulo with zero.")
                return num1 % num2
        except ZeroDivisionError as e:
            print(e)
            return None
        except ValueError as e:
            print(e)
            return None

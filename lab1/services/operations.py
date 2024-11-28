import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y

def exponentiate(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        raise ValueError("Square root of a negative number is not defined.")
    return math.sqrt(x)

def modulo(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero for modulo operation is not allowed.")
    return x % y

def calculate(num1, operator, num2):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    elif operator == '^':
        return exponentiate(num1, num2)
    elif operator == '√':
        return sqrt(num1)
    elif operator == '%':
        return modulo(num1, num2)
    else:
        raise ValueError(f"Invalid operator: {operator}")

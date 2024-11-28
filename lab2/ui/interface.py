import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from lab2.services.calculator import Calculator


if __name__ == "__main__":
    calculator = Calculator(decimal_places=2)
    calculator.run()

import unittest
from calculator.main import calculate
from calculator.memory import Memory
from calculator.history import History

class TestMain(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()
        self.history = History()

    def test_basic_calculations(self):
        self.assertEqual(calculate(4, '+', 3), 7)
        self.assertEqual(calculate(10, '-', 3), 7)
        self.assertEqual(calculate(3, '*', 4), 12)
        self.assertEqual(calculate(8, '/', 2), 4)

    def test_invalid_operation(self):
        result = calculate(10, '&', 5)
        self.assertIsNone(result)

    def test_divide_by_zero(self):
        result = calculate(10, '/', 0)
        self.assertIsNone(result)

    def test_sqrt_of_negative(self):
        result = calculate(-1, '√', None)
        self.assertIsNone(result)

    def test_exponentiate(self):
        self.assertEqual(calculate(2, '^', 3), 8)

    def test_modulo(self):
        self.assertEqual(calculate(10, '%', 3), 1)

    def test_memory_integration(self):
        self.memory.store(15)
        self.assertEqual(self.memory.retrieve(), 15)

    def test_history_integration(self):
        self.history.add_entry(5, '*', 5, 25)
        self.assertEqual(len(self.history.entries), 1)
        self.assertEqual(self.history.entries[0], "5 * 5 = 25")

if __name__ == "__main__":
    unittest.main()

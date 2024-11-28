import unittest
from calculator.operations import add, subtract, multiply, divide, exponentiate, sqrt, modulo

class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-3, -5), -8)
        self.assertEqual(add(-3, 5), 2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(4, 10), -6)
        self.assertEqual(subtract(-3, -5), 2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-3, 7), -21)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(9, 3), 3)

    def test_divide_by_zero(self):
        result = divide(10, 0)
        self.assertIsNone(result)

    def test_exponentiate(self):
        self.assertEqual(exponentiate(2, 3), 8)

    def test_sqrt_positive(self):
        self.assertEqual(sqrt(16), 4)

    def test_sqrt_negative(self):
        self.assertIsNone(sqrt(-1))

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)

if __name__ == "__main__":
    unittest.main()
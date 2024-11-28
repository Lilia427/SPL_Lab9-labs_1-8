import unittest
from calculator.settings import Settings

class TestSettings(unittest.TestCase):
    def setUp(self):
        self.settings = Settings()

    def test_set_decimal_places(self):
        self.settings.set_decimal_places(3)
        self.assertEqual(self.settings.decimal_places, 3)

    def test_round_result(self):
        self.assertEqual(self.settings.round_result(3.14159), 3.142)
        self.assertEqual(self.settings.round_result(2.71828), 2.718)

    def test_invalid_decimal_places(self):
        with self.assertRaises(ValueError):
            self.settings.set_decimal_places(-1)

if __name__ == "__main__":
    unittest.main()

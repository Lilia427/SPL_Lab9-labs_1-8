import unittest
from calculator.history import History
from io import StringIO
import sys

class TestHistory(unittest.TestCase):
    def setUp(self):
        self.history = History()

    def test_add_entry(self):
        self.history.add_entry(3, '+', 2, 5)
        self.assertEqual(len(self.history.entries), 1)
        self.assertEqual(self.history.entries[0], "3 + 2 = 5")

    def test_show_empty_history(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.history.show()
        sys.stdout = sys.__stdout__
        self.assertIn("No history available.", captured_output.getvalue().strip())

    def test_show_history_with_entries(self):
        self.history.add_entry(3, '+', 2, 5)
        captured_output = StringIO()
        sys.stdout = captured_output
        self.history.show()
        sys.stdout = sys.__stdout__
        self.assertIn("3 + 2 = 5", captured_output.getvalue().strip())

    def test_clear_history(self):
        self.history.add_entry(3, '+', 2, 5)
        self.history.clear()
        self.assertEqual(len(self.history.entries), 0)

if __name__ == "__main__":
    unittest.main()

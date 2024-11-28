import unittest
from calculator.memory import Memory

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()

    def test_store_value(self):
        self.memory.store(42)
        self.assertEqual(self.memory.memory, 42)

    def test_retrieve_value(self):
        self.memory.store(100)
        self.assertEqual(self.memory.retrieve(), 100)

    def test_retrieve_no_value(self):
        self.assertIsNone(self.memory.retrieve())

    def test_clear_memory(self):
        self.memory.store(200)
        self.memory.clear()
        self.assertIsNone(self.memory.retrieve())

if __name__ == "__main__":
    unittest.main()

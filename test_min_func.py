import unittest
from min_func import minimum

class TestMinimum(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(minimum([5]), 5)

    def test_sorted_list(self):
        self.assertEqual(minimum([1, 2, 3]), 1)

    def test_unsorted_list(self):
        self.assertEqual(minimum([3, 1, 4, 2]), 1)

    def test_negative_numbers(self):
        self.assertEqual(minimum([-5, -1, -3]), -5)

    def test_mixed_numbers(self):
        self.assertEqual(minimum([0, -1, 10, -20]), -20)

    def large_mixed_numbers(self):
        self.assertEqual(minimum([-21, 20, 0, 4, 6, 34, 40, 0, -1, -1, 6, 45, -4]), -21)

if __name__ == "__main__":
    unittest.main()
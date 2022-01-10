import unittest
from array1 import Solution


class TestSortedSquares(unittest.TestCase):
    def setUp(self):
        self.array1 = Solution()

    def test_empty_nums(self):
        self.assertEqual(self.array1.sortedSquares([]), [])

    def test_mixed_nums(self):
        result = self.array1.sortedSquares([-4, -1, 0, 3, 10])
        expected = [0, 1, 9, 16, 100]
        self.assertEqual(result, expected)

    def test_positive_nums(self):
        self.assertEqual(self.array1.sortedSquares([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    def test_negative_nums(self):
        self.assertEqual(self.array1.sortedSquares([-5, -4, -3, -2, -1]), [1, 4, 9, 16, 25])
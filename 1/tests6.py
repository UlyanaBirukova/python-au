import unittest
from linked_list6 import Solution


class TestsortList(unittest.TestCase):
    def setUp(self):
        self.linked_list6 = Solution()

    def test_empty_nums(self):
        self.assertEqual(self.linked_list6.sortList([]), [])

    def test_mixed_nums(self):
        result = self.linked_list6.sortList([-1, 5, 3, 4, 0])
        expected = [-1, 0, 3, 4, 5]
        self.assertEqual(result, expected)

    def test_positive_nums(self):
        self.assertEqual(self.linked_list6.sortList([4, 2, 1, 3]), [1, 2, 3, 4])

    def test_negative_nums(self):
        self.assertEqual(self.linked_list6.sortList([-5, -4, -3, -1, -2]), [-5, -4, -3, -2, -1])
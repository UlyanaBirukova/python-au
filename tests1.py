import unittest
from linked_list1 import Solution


class TestReverseList(unittest.TestCase):
    def setUp(self):
        self.linked_list1 = Solution()

    def test_empty(self):
        self.assertEqual(self.linked_list1.reverseList([]), [])

    def test(self):
        result = self.linked_list1.reverseList([1, 2, 3, 4, 5])
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(result, expected)
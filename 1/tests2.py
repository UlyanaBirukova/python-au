import unittest
from linked_list2 import Solution


class TestMiddleNode(unittest.TestCase):
    def setUp(self):
        self.linked_list2 = Solution()

    def test_empty(self):
        self.assertEqual(self.linked_list2.middleNode([]), [])

    def test(self):
        result = self.linked_list2.middleNode([1, 2, 3, 4, 5])
        expected = [3, 4, 5]
        self.assertEqual(result, expected)
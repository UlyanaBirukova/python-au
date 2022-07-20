import unittest
from linked_list4 import Solution


class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.linked_list4 = Solution()

    def test_empty_all(self):
        self.assertEqual(self.linked_list4.mergeTwoLists([],[]), [])

    def test_empty_one(self):
        result = self.linked_list4.mergeTwoLists([],[0])
        expected = [0]
        self.assertEqual(result, expected)

    def test(self):
        self.assertEqual(self.solution.mergeTwoLists([1, 2, 3], [1, 3, 4]), [1, 1, 2, 3, 4, 4])

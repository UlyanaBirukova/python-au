import unittest
from linked_list3 import Solution


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.linked_list3 = Solution()

    def test_empty(self):
        self.assertEqual(self.linked_list3.isPalindrome([]), true)

    def test_true(self):
        result = self.linked_list3.isPalindrome([1, 2, 2, 1])
        expected = true
        self.assertEqual(result, expected)

    def test_false(self):
        self.assertEqual(self.linked_list3.isPalindrome([1, 2]), false)

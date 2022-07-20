import unittest
from linked_list5 import Solution


class TestGetIntersectionNode(unittest.TestCase):
    def setUp(self):
        self.linked_list5 = Solution()

    def test(self):
        self.assertEqual(self.linked_list5.getIntersectionNode([8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3), 8)

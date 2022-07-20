class Solution:
    def merge_lists(self, l1, l2):
        res = []
        while l1 and l2:
            res.append((l1 if l1[-1] > l2[-1] else l2).pop())
        return (res + l1[-1::-1] + l2[-1::-1])[-1::-1]

    def find_index_of_first_nonnegative(self, l):
        for i, el in enumerate(l):
            if el >= 0:
                return i

    def sortedSquares(self, nums: List[int]) -> List[int]:
        sep_index = self.find_index_of_first_nonnegative(nums)
        were_negative = list(map(abs, nums[:sep_index]))[::-1]
        were_not_negative = list(nums[sep_index:]) if sep_index != None else []
        return list(map(lambda x: x * x, self.merge_lists(were_negative, were_not_negative)))

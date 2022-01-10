# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def c(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            new_prev = cur
            new_nxt = prev
            new_cur = cur.next
            prev = new_prev
            cur.next = new_nxt
            cur = new_cur
        return prev

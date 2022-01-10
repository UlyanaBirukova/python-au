# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_middle(self, head):
        slow = fast = head
        while fast != None and fast.next != None:
            fast, slow = fast.next.next, slow.next
        return slow


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = self.find_middle(head)
        node = None
        while slow != None:
            slow.next, node, slow = node, slow, slow.next
        while node != None:
            if node.val != head.val:
                return False
            else:
                node, head = node.next, head.next
        return True
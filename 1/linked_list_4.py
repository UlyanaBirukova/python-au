# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = ListNode(0)
        zero_node = a
        while (list1 != None and list2 != None):
            if (list1.val <= list2.val):
                a.next = list1
                list1 = list1.next
            else:
                a.next = list2
                list2 = list2.next
            a = a.next

        if list1 == None:
            list1 = list2
        while (list1 != None):
            a.next = list1
            list1 = list1.next
            a = a.next

        return zero_node.next

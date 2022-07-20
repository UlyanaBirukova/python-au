# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        midPrev = None
        while (head != None and head.next != None):
            midPrev = head if (midPrev == None) else midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid


    def merge(self, list1, list2):
        cur = ListNode()
        tail = cur
        while (list1 != None and list2 != None):
            if (list1.val < list2.val):
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        tail.next = list1 if (list1 != None) else list2
        return cur.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def ll_len(self, head):
            temp = head
            n = 0
            while temp:
                n +=1
                temp = temp.next
            return n

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n1 = self.ll_len(headA)
        n2 = self.ll_len(headB)
        if n1 < n2:
            headA, headB, n1, n2 = headB, headA, n2, n1
        diff = n1 - n2
        tempA = headA
        for i in range(diff, 0, -1):
            tempA = tempA.next
        tempB = headB
        while tempA:
            if tempA == tempB:
                return tempA
            else:
                tempA, tempB = tempA.next, tempB.next
        return None
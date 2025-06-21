#Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visit = set()
        A = headA
        B = headB
        while (A):
            visit.add(A)
            A = A.next
       
        while B :
            if B in visit:
                return B
            B = B.next
        return
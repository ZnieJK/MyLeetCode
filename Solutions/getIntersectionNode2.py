#Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        cur_a = headA
        cur_b = headB
        
        while cur_a != cur_b:
            if cur_a:
                cur_a = cur_a.next
            else:
                cur_a = headB
            if cur_b:
                cur_b = cur_b.next
            else:
                cur_b = headA
            
        return cur_a
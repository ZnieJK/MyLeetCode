# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
       
        if not head:
            return head
       
        if head.val == val and not head.next:
            return None




        temp = self.removeElements(head.next,val)
        curr = head
        if curr.val == val:
            return temp        
        curr.next = temp


        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
       
        if list1.val < list2.val:
            head = list1
            oth_head_it = list2
        else:
            head = list2
            oth_head_it = list1


        ans = head
        curr_head_it = head.next


        while curr_head_it:
            if curr_head_it.val <= oth_head_it.val:
                head = curr_head_it
                curr_head_it = curr_head_it.next
            else:
                tmp = head.next
                head.next = oth_head_it
                head = oth_head_it
                curr_head_it = oth_head_it.next
                oth_head_it = tmp


        head.next = oth_head_it
        head = oth_head_it


        return ans

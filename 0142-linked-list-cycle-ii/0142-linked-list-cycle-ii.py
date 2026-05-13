# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d={}
        curr=head
        if not head or not head.next:
            return None
        while curr:
            d[curr]=True
            if curr.next in d:
                return curr.next
            curr=curr.next
        return None
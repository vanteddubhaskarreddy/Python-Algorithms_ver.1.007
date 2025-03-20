# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        shead = fhead = head
        while fhead and fhead.next: shead, fhead = shead.next, fhead.next.next
        return shead
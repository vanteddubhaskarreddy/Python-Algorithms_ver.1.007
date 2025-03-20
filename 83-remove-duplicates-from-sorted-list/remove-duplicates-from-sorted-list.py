# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        s = set()
        while dummy:
            s.add(dummy.val)
            if dummy.next and dummy.next.val in s: dummy.next = dummy.next.next
            else :dummy = dummy.next
        return head
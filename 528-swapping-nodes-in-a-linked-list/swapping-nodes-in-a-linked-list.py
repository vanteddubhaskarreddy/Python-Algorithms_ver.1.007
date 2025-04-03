# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fp = one = two = head
        while k > 1:
            one, fp = one.next, fp.next
            k -= 1
        while fp.next:
            fp, two = fp.next, two.next
        one.val, two.val = two.val, one.val

        return head
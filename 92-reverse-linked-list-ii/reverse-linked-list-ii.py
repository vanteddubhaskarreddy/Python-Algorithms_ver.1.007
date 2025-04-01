# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        d = right - left
        r = l = head
        if left == right:
            return head
        while d > 0:
            r = r.next
            d -= 1
        while left > 2:
            r = r.next
            l = l.next
            left -= 1
        if left > 1:
            bl = l
            l, r = l.next, r.next
            bl.next = r
        ar, prev, curr = r.next, l, l.next
        nextnode, l.next = curr.next, ar
        while prev != r:
            curr.next = prev
            prev = curr
            curr = nextnode
            if nextnode:
                nextnode = nextnode.next   
            else:
                break
        return head if left > 1 else r
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        d = right - left
        left_start = left
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
        if left_start>1:
            bl = l
            l = l.next
            r = r.next 
            bl.next = r
        else: 
            bl = None
        # l = l.next
        # r = r.next
        ar = r.next
        prev = l
        curr = l.next
        nextnode = curr.next
        l.next = ar
        while prev != r:
            curr.next = prev
            prev = curr
            curr = nextnode
            if nextnode:
                nextnode = nextnode.next   
            else:
                break
        return head if left_start > 1 else r
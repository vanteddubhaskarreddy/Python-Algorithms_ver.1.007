# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head.next
        slow = head
        n = 2
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            n+=2
        prev = None
        curr = slow.next
        nextnode = curr.next
        slow.next = fast
        while nextnode:
            curr.next = prev
            prev = curr
            curr = nextnode
            nextnode = nextnode.next
        curr.next = prev

        first = head 
        second = fast
        maxv = 0
        while second:
            print(first.val)
            print(second.val)
            value = first.val + second.val
            print(value)
            maxv = max(value, maxv)
            first = first.next
            second = second.next
        return maxv
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = head
        while head and head.next and (head.val == head.next.val):
            while dummy and (dummy.val == head.val):
                dummy = dummy.next
            head = dummy
        
        slow = fast = dummy = head
        while slow:
            dummy = slow.next
            fast = slow.next
            while slow.next and slow.next.next and (slow.next.val == slow.next.next.val):
                if fast.val == dummy.val:
                    fast = fast.next
                    if not fast:
                        slow.next = fast
                        break
                else:
                    slow.next = fast
                    dummy = fast = slow.next
            slow = slow.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        current = slow
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        first_half = head
        second_half = prev
        is_palindrome = True
        
        while second_half:
            if first_half.val != second_half.val:
                is_palindrome = False
                break
            first_half = first_half.next
            second_half = second_half.next
        
        current = prev
        prev = None
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        return is_palindrome
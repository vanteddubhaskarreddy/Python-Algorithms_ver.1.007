# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         i = 0
#         j = len(s) - 1
#         c = 0
#         while i < j:
#             if s[i] != s[j]:
#                 if c == 0:
#                     c = 1
#                     if s[i+1] == s[j] and s[i+2] == s[j-1] and s[i+3] == s[j-2]:
#                         i = i+1
#                         # print('i+1')
#                         # print(i)
#                         # print(j)
#                         # print(s[i])
#                         # print(s[j])
#                         # print(s)
#                         # print('\n\n\n')
                        
#                     elif s[i] == s[j-1]:
#                         j = j-1
#                         # print('j-1')
#                         # print(i)
#                         # print(j)
#                         # print(s[i])
#                         # print(s[j])
#                         # print('\n\n\n')

#                     else:
#                         # print(i)
#                         # print(j)
#                         # print(s[i])
#                         # print(s[j])
#                         return False
#                 else:
#                     # print(i)
#                     # print(j)
#                     # print(s[i])
#                     # print(s[j])
#                     # print(len(s))
#                     # print(s)
#                     return False
#             i,j = i+1,j-1
#         return True

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True
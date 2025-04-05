class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        print(s[1:])
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
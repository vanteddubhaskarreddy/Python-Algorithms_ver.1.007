class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            
            if stack and abs(ord(stack[-1]) - ord(i)) == 32:
                print(i, ord(i), stack[-1], ord(stack[-1]))
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for c in s:
            if stack1 and c == '#':
                stack1.pop()
            elif c != '#':
                stack1.append(c)
        for d in t:
            if stack2 and d == '#':
                stack2.pop()
            elif d != '#':
                stack2.append(d)
        return True if stack1 == stack2 else False
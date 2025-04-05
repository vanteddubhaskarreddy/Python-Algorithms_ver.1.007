class Solution:
    def isValid(self, s: str) -> bool:
        o_stack = []
        for c in s:
            if c in ('(', '[', '{'):
                o_stack.append(c)
            elif c in (')', ']', '}'):
                if o_stack and (ord(o_stack[-1])+1 == ord(c) or ord(o_stack[-1])+2 == ord(c)):
                    o_stack.pop()
                else :
                    return False
        return True if not o_stack else False
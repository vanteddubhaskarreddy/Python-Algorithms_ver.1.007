class Solution:
    def simplifyPath(self, path: str) -> str:
        s = [item for item in path.split('/') if item]
        res = []
        for i in s:
            if res and i == '..':
                res.pop()
            elif i == '.':
                pass
            elif i not in ('..', '.'):
                res.append(i)
        return '/'+'/'.join(res)
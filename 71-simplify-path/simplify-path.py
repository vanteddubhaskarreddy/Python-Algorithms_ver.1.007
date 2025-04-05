class Solution:
    def simplifyPath(self, path: str) -> str:
        ts = path.split('/')
        s = [item for item in ts if item]
        print(s)
        res = []
        for i in s:
            if res and i == '..':
                res.pop()
            elif i == '.':
                continue
            elif i not in ('..', '.'):
                res.append(i)
        return '/'+'/'.join(res)
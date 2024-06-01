class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in operations:
            try:
                res.append(int(i))
            except:
                if i == '+':
                    res.append(res[-1]+res[-2])
                elif i == 'D':
                    res.append(res[-1]+res[-1])
                else:
                    res.pop()
        return sum(res)
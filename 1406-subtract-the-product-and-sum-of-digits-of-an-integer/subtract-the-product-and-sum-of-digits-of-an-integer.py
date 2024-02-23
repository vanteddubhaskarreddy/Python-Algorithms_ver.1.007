class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m = str(n)
        s = 0
        p = 1
        for i in m:
            i = int(i)
            s,p = s+i,p*i
        return p-s
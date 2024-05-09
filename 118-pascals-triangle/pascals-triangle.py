class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1])
        if numRows < 3:
            if numRows <2:
                return res
            res.append([1,1])
            return res
        res.append([1,1])
        n=2
        while n<numRows:
            i=1
            temp=[]
            prev=res[-1]
            temp.append(1)
            for i in range(1,n):
                
                temp.append(prev[i-1]+prev[i])
            temp.append(1)
            res.append(temp)
            n+=1
        
        return res
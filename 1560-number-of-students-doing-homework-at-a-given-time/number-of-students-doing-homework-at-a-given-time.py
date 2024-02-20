class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        r=0
        for i,j in zip(startTime,endTime):
            if i<=queryTime and j>=queryTime:
                r+=1
        return r
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        s = 0
        i = len(grid)-1
        j = 0
        n = len(grid[0])
        while i>=0:
            if j == n:
                j = 0
                i = i-1
            elif grid[i][j] < 0:
                s = s+(n-j)
                j = 0
                i = i-1
            else:
                j+=1
            
        return s
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        seen = set()
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return 0
        ans = 0

        def isValid(c, d):
            return True if 0 <= c < m and 0 <= d < n and (c, d) not in seen and grid[c][d] == 1 else False

        def dfs(a, b):
            cur_area=1
            for x, y in directions:
                c, d = a+x, b+y
                
                if isValid(c, d):
                    seen.add((c, d))
                    cur_area+=dfs(c, d)
            return cur_area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if (i, j) not in seen:
                        seen.add((i, j))
                        ans=max(dfs(i, j), ans)
        
        return ans
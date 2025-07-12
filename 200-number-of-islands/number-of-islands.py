class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        travel_options = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        ans = 0
        r = len(grid)
        c = len(grid[0])

        def is_valid(a, b):
            return True if 0 <= a < r and 0<= b < c and grid[a][b] == '1' and (a, b) not in seen else False

        def dfs(m,n):
            for x,y in travel_options:
                if is_valid(m+x, n+y):
                    seen.add((m+x, n+y))
                    dfs(m+x, n+y)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and (i, j) not in seen:
                    seen.add((i,j))
                    ans+=1
                    # print(i, j, ans, seen)
                    dfs(i,j)
        
        return ans
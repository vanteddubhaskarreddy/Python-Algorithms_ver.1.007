class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        seen = {(0,0)}
        q = deque([(0,0,1)])
        directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        n = len(grid)
        def is_valid(x, y):
            return True if 0<=x<n and 0<=y<n and grid[x][y] == 0 and (x, y) not in seen else False
        
        while q:
            row, col, count = q.popleft()

            if (row, col) == (n-1, n-1):
                return count

            for dx, dy in directions:
                nx, ny = row+dx, col+dy
                if is_valid(nx, ny):
                    seen.add((nx, ny))
                    q.append((nx, ny, count+1))
        
        return -1
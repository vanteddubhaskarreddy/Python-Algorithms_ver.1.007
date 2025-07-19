class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def is_valid(row, col):
            return True if 0<=row<m and 0<=col<n and maze[row][col] == '.' and (row, col) not in seen else False

        def is_exit(row, col):
            return True if (row in (0, m-1) or col in (0, n-1)) and is_valid(row, col) else False

        start_row = entrance[0]
        start_col = entrance[1]
        seen = {(start_row, start_col)}
        q = deque([(start_row, start_col, 0)])
        m = len(maze)
        n = len(maze[0])
        directions = ((0,-1), (-1,0),(0,1),(1,0))

        while q:
            row, col, steps = q.popleft()

            for dx, dy in directions:
                nx, ny = row+dx, col+dy
                if is_exit(nx, ny):
                    return steps+1
                elif is_valid(nx, ny):
                    q.append((nx, ny, steps+1))
                    seen.add((nx, ny))
        
        return -1
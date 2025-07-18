class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def is_valid(a, b):
            return True if (a, b) not in seen and 0<=a<m and 0<=b<n and mat[a][b] == 1 else False
        
        q = deque()
        seen = set()
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j,1))
                    seen.add((i,j))
        
        directions = ((0, -1), (-1, 0), (0, 1), (1, 0))

        while q:
            x, y, steps = q.popleft()
            for dx, dy in directions:
                i, j = x+dx, y+dy
                if is_valid(i,j):
                    seen.add((i,j))
                    q.append((i,j,steps+1))
                    mat[i][j] = steps
        
        return mat
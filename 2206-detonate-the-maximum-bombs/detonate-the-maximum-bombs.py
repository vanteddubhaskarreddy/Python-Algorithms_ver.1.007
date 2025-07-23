from math import pow as pow
from math import sqrt
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(set)

        for i in range(len(bombs)):
            x1, y1, d1 = bombs[i][0], bombs[i][1], bombs[i][2]
            for j in range(i, len(bombs)):
                x2, y2, d2 = bombs[j][0], bombs[j][1], bombs[j][2]
                if i != j:
                    d = sqrt(pow(x2-x1, 2) + pow(y2-y1,2))
                    if  d<= d1:
                        graph[i].add(j)
                    if d <= d2:
                        graph[j].add(i)

        def bfs(i):
            q = deque([i])
            seen = set([i])

            while q:
                node = q.popleft()
                for neighbour in graph[node]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        q.append(neighbour)
            return len(seen)
        
        answer = 0

        for i in range(len(bombs)):
            answer = max(answer, bfs(i))
        
        return answer
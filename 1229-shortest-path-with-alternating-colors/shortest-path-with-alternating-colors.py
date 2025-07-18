class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        r = 0
        b = 1
        graph = defaultdict(lambda:defaultdict(list))
        for x, y in redEdges:
            graph[x][r].append(y)
        for x, y in blueEdges:
            graph[x][b].append(y)
        
        ans = [float('inf')]*n
        q = deque([(0,r,0), (0,b,0)])
        seen = {(0,r), (0,b)}
        while q:
            node, color, steps = q.popleft()
            ans[node] = min(ans[node], steps)
            for neighbour in graph[node][color]:
                if (neighbour, 1-color) not in seen:
                    seen.add((neighbour, 1-color))
                    q.append((neighbour, 1-color, steps+1))
        
        return [x if x!=float('inf') else -1 for x in ans]
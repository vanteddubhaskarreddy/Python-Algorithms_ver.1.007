class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(values)):
            val = values[i]
            n,d = equations[i]
            graph[n][d] = val
            graph[d][n] = 1/val
        
        def bfs(n,d):
            if n not in graph:
                return -1
            
            seen = {n}
            q = deque([(n,1)])
            while q:
                node, val = q.popleft()
                if node == d:
                    return val
                for neighbour in graph[node]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        q.append((neighbour, val*graph[node][neighbour]))
            return -1
        
        ans = []
        for n,d in queries:
            ans.append(bfs(n,d))
        return ans
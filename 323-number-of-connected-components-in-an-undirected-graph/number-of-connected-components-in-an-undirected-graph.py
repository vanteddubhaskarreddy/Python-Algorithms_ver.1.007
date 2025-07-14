class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        seen = set()

        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)

        ans = 0
        for x in graph:
            if x not in seen:
                ans+=1
                seen.add(x)
                dfs(x)
        
        return ans + (n - len(seen))
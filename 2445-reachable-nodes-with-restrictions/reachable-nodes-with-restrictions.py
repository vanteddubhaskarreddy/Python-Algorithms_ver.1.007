class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        seen={0}
        restricted = set(restricted)
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            ans = 1
            for neighbour in graph[node]:
                if neighbour not in seen and neighbour not in restricted:
                    seen.add(neighbour)
                    ans+=dfs(neighbour)
            return ans

        return dfs(0)
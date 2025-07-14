class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        seen = {source}
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in seen:
                    if neighbour == destination:
                        seen.add(neighbour)
                        break
                    seen.add(neighbour)
                    dfs(neighbour)
        
        dfs(source)

        return True if destination in seen else False
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = {0}
        def dfs(node):
            for neighbour in rooms[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)
        
        dfs(0)
        return len(seen) == len(rooms) 
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        graph = defaultdict(list)
        n = len(arr)
        for i in range(n):
            front, back = i+arr[i], i-arr[i]
            if front < n:
                graph[i].append(front)
            if back > -1:
                graph[i].append(back)
        
        q = deque([start])
        seen = {start}

        while q:
            node = q.popleft()
            if arr[node] == 0:
                return True
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    q.append(neighbour)
        return False
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)
        if '0000' in seen:
            return -1
        seen.add('0000')
        q = deque([('0000', 0)])

        def directions(node):
            ans = []
            for i in range(4):
                for j in [-1,1]:
                    new_num = (int(node[i])+j) % 10
                    ans.append(node[:i]+str(new_num)+node[i+1:])
            return ans

        while q:
            curr, steps = q.popleft()
            if curr == target:
                return steps
            for node in directions(curr):
                if node not in seen:
                    q.append((node, steps+1))
                    seen.add(node)
        return -1
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        seen = {startGene}
        q = deque([(startGene, 0)])
        n = 8

        neighbours = ['A', 'C', 'G', 'T']

        while q:
            gene, steps = q.popleft()
            if gene == endGene:
                return steps
            for neighbour in neighbours:
                for i in range(n):
                    ngene = gene[:i]+neighbour+gene[i+1:]
                    if ngene not in seen and ngene in bank:
                        seen.add(ngene)
                        q.append((ngene, steps+1))
        
        return -1
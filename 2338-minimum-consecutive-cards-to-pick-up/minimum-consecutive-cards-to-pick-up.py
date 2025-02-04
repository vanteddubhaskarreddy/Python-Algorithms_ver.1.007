class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = defaultdict(list)
        mins = float(inf)
        for i in range(len(cards)):
            if cards[i] in d:
                mins = min(mins, 1+i - d[cards[i]])
                d[cards[i]] = i
            else:
                d[cards[i]] = i
        return mins if mins != float(inf) else -1
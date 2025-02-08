class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = Counter(stones)
        sm = 0
        for i in jewels: 
            if i in s: sm+=s[i]
        return sm
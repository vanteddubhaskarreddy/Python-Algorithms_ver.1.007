class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = set()
        for i in sentence:
            d.add(i)
        return True if len(d) == 26 else False
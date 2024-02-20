class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = sentence.split()
        for i in range(len(l)):
            if searchWord == l[i][:len(searchWord)]:
                return i+1
        return -1
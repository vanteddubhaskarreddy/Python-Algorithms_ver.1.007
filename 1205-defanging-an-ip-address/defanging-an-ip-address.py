class Solution:
    def defangIPaddr(self, address: str) -> str:
        l = list(address)
        for i in range(1,len(l)-1):
            if l[i] == '.':
                l[i] = '[.]'
        return ''.join(l)
class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        c = 0
        for i in arr:
            if i+1 in s:
                c+=1
        return c


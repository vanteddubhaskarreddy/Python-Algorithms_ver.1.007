class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0 for i in range(len(temp))]
        index = []
        for i in range(len(temp)):
            while index and temp[index[-1]] < temp[i]:
                res[index[-1]] = i - index[-1]
                index.pop()
            index.append(i)
        return res
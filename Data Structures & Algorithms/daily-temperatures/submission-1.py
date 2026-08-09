class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, t in enumerate(temperatures):
            if len(stack) > 0 and stack[-1][0] < t:
                while len(stack) > 0 and t > stack[-1][0]:
                    temp, ind = stack.pop()
                    res[ind] = index - ind
            stack.append((t, index))

        return res
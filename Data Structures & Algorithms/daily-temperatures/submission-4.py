class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # [index, temperature]

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                ind, tmp = stack.pop()
                result[ind] = index - ind
            stack.append([index, temp])

        return result

        
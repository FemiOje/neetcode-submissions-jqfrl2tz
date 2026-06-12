class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            currentDay = temperatures[i]
            daysAfter = 0

            for j in range(i, len(temperatures)):
                if temperatures[j] > currentDay:
                    result[i] = j - i   
                    break 

        return result
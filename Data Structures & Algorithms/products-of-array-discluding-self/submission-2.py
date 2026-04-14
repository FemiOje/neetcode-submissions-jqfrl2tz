class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for index1, num in enumerate(nums):
            temp = 1
            for index2, num2 in enumerate(nums):
                if index1 != index2:
                    temp *= num2
            result.append(temp)
            temp = 1

        return result
        
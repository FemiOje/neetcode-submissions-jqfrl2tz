class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffMap = dict()

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in diffMap:
                return [diffMap[difference], i]
            
            diffMap[nums[i]] = i
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        result = 1
        current_streak = 1
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                if nums[i - 1] == nums[i] - 1:
                    current_streak += 1
                else:
                    result = max(result, current_streak)
                    current_streak = 1
            i += 1

        return max(result, current_streak)
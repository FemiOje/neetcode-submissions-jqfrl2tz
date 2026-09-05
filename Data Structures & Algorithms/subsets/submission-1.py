class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(n):
            # base case: n is out of array nums bounds
            if n >= len(nums):
                result.append(subset.copy())
                return
            
            # explore the depth of the branch including nums[n]
            subset.append(nums[n])
            dfs(n + 1)

            # explore the depth of the branch excluding nums[n]
            subset.pop()
            dfs(n + 1)
        
        dfs(0)
        return result
        
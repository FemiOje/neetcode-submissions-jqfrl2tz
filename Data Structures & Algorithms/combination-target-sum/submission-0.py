class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(n, curr, total):
            if total > target or n >= len(nums):
                return
            if total == target:
                result.append(curr.copy())
                return

            curr.append(nums[n])
            dfs(n, curr, total + nums[n])

            curr.pop()
            dfs(n+1, curr, total)

        dfs(0, [], 0)
        return result

        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l = 0
        freq = {}
        maxTemp = float('-inf')


        # first pass
        for i in range(k):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
            if nums[i] > maxTemp: maxTemp = nums[i] 
        
        result.append(maxTemp)

        if len(nums) == k:
            return result

        # sliding window
        for r in range(k, len(nums)):
            maxTemp = float('-inf')
            freq[nums[l]] -= 1
            l += 1

            freq[nums[r]] = 1 + freq.get(nums[r], 0)

            for key, value in freq.items():
                if key in freq and value > 0:
                    if key > maxTemp: maxTemp = key 
            
            result.append(maxTemp)



        return result

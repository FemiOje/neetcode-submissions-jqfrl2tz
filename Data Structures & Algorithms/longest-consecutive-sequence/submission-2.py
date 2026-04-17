class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        maxLength = 0

        if not nums:
            return 0

        for num in nums:
            s.add(num)

        for num in nums:
            length = 1

            if (num - 1) in s: 
                continue
            
            k = num
            while k + 1 in s:
                length += 1
                k += 1

            maxLength = max(length, maxLength)
         

        return maxLength
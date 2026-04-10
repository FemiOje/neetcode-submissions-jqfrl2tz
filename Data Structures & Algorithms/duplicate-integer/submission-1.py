class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set(())

        for each in nums:
            if each not in numSet:
                numSet.add(each)
            else:
                return True
        
        return False
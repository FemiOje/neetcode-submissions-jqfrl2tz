class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(numbers)):
            difference = target - numbers[i]
            
            if difference in hashMap:
                return [min(i+1, hashMap.get(difference)), max(i+1, hashMap.get(difference))]
            
            hashMap[numbers[i]] = i+1
        
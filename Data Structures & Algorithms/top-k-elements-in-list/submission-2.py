class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        l = [[] for i in range(len(nums) + 1)]

        for number in nums:
            freq[number] = 1 + freq.get(number, 0)
        
        for a, b in freq.items():
            l[b].append(a)

        result = []

        for number in range(len(l) - 1, 0, -1):
            for num in l[number]:
                result.append(num)
                if len(result) == k:
                    return result

        
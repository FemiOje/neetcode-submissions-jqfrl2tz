class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = l + (r - l) // 2
            hours = 0

            for i in range(len(piles)):
                hours += math.ceil(piles[i] / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1


        return res
        
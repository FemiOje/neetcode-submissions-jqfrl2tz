class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        minLR = [0] * len(height)
        res = 0

        for i in range(len(height)):
            if i == 0:
                continue
            
            maxLeft[i] = max(height[i - 1], maxLeft[i - 1])


        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                continue
            
            maxRight[i] = max(height[i + 1], maxRight[i + 1])

        for i in range(len(height)):
            minLR[i] = min(maxLeft[i], maxRight[i])

            if minLR[i] - height[i] >=0:
                res += minLR[i] - height[i]


        return res

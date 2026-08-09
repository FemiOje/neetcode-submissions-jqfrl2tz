class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()

            p1 = stones.pop()
            p2 = stones.pop()

            diff = p1 - p2

            if diff != 0:
                stones.append(diff)


        return stones[0] if len(stones) > 0 else 0
        
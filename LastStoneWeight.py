class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
            
        heapify(stones)

        while len(stones) > 1:
            stone1, stone2 = -1* heappop(stones), -1 * heappop(stones)
            if stone1 != stone2:
                heappush(stones,-1 * (stone1 - stone2))

        return 0 if not stones else -1* heappop(stones)

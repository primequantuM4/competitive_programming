class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1

        heapify(piles)

        for _ in range(k):
            big_stone_piles = heappop(piles) // 2
            heappush(piles, big_stone_piles)
        
        return -1 * sum(piles)

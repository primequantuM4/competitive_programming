class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.play(1, 0, len(nums) - 1, nums) >= 0
        

    def play(self, player, left, right, nums):
        if left == right:
            return nums[left] * player
        
        leftPlay = self.play(-player, left+1, right, nums) + nums[left] * player
        rightPlay = player * nums[right] + self.play(-player, left, right - 1, nums)

        if player == 1:
            return max(leftPlay, rightPlay)
        else:
            return min(leftPlay, rightPlay)

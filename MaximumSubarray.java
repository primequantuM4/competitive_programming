class Solution {
    public int maxSubArray(int[] nums) {
        int maxSub = nums[0];
        int ptr = 0;
        for (int i : nums){
            if (ptr < 0){
                ptr = 0;
            }
            ptr += i;
            maxSub = Math.max(maxSub, ptr);
        }
        return maxSub;
    }
}

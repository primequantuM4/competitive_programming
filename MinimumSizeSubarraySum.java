class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int total = 0;
        int res = nums.length + 1;
        for (int i = 0; i <  nums.length; i++){
            total += nums[i];
            while (total >= target){
                res =  Math.min(i - left + 1, res);
                total -= nums[left];
                left += 1;
                
            }
        }
        if (res == nums.length + 1) return 0;
        else return res;
    }
}

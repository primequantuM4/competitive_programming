class Solution {
    public int longestSubarray(int[] nums) {
        int left =0;
        int count = 0;
        int zeroes = 0;
        int max = 0;
        for (int right = 0; right < nums.length; right++){
            if (nums[right] == 0) zeroes++;
            if (zeroes < 2){
                count ++;
            }else{
                left ++;
                if (nums[left - 1] == 0) zeroes --;
            }
            max = Math.max(count, max);
        }
        return max - 1;
    }
}

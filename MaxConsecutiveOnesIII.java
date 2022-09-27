class Solution {
    public int longestOnes(int[] nums, int k) {
        int leftpointer = 0;
        int size = nums.length;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == 0) k--;
            if (k < 0){
                if (nums[leftpointer] == 0){
                    k ++;
                }
                leftpointer ++;
            }
        }
        return size - leftpointer;
    }
}

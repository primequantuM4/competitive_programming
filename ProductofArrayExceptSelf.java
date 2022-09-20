class Solution {
    public int[] productExceptSelf(int[] nums) {
        int leftptr = 1;
        int rightptr = 1;
        int[] ans = new int[nums.length];
        for (int i = 0; i < nums.length; i++){
            ans[i] = leftptr;
            leftptr *= nums[i];
        }
        for (int i = nums.length - 1; i >= 0; i--){
            ans[i] *= rightptr;
            rightptr *= nums[i];
        }
        return ans;
    }
}

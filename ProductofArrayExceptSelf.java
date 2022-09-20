class Solution {
    public int[] productExceptSelf(int[] nums) {
        int leftptr = 1; 
        int rightptr = 1; 
        int[] ans = new int[nums.length];
        int[] left = new int[nums.length]; 
        int[] right = new int[nums.length];
        for (int i = 0; i < nums.length; i++){
            left[i] = leftptr;
            leftptr *= nums[i];
        }
        for (int i = nums.length - 1; i >= 0; i--){
            right[i] = rightptr;
            rightptr *= nums[i];
        }
        for (int i = 0; i < nums.length; i++){
            ans[i] = left[i] * right[i];
        }
        return ans;
    }
}


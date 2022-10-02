class Solution {
    public int pivotIndex(int[] nums) {}
        int prevSum = 0;
        int nextSum = 0;
        int[] ans = new int[nums.length];
        ans[0] = nums[0];
        for (int i = 1; i < nums.length; i++){
            ans[i] = ans[i - 1] + nums[i];
        }
        for (int i = 0; i< nums.length; i++){
            prevSum = ans[i] - nums[i];
            nextSum = ans[ans.length -1] - ans[i];
            if (prevSum == nextSum){
                return i;
            }
        }
        return -1;
    }
}

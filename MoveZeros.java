class Solution {
    public void moveZeroes(int[] nums) {
        int leftptr = 0;
        int temp;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] != 0){
                temp = nums[i];
                nums[i] = nums[leftptr];
                nums[leftptr] = temp;
                leftptr ++;
                
            }
        }
    }
}

class Solution {
    public int subarrayGCD(int[] nums, int k) {
        int subArrayCount = 0;

        for (int i = 0; i < nums.length; i++){
            int currGCD = nums[i];
            if (nums[i] == k) subArrayCount ++;
            for (int j = i+1; j< nums.length; j++){
                if (nums[j] < k) break;

                currGCD = getGCD(nums[j], currGCD);
                if (currGCD == k) subArrayCount++;
            }
        }
        return subArrayCount;
    }
    public int getGCD(int x, int y){
        while(y!=0){
            int remainder = x%y;
            x = y;
            y = remainder;
        }
        return x;
    }
}

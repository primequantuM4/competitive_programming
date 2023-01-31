class Solution {
    public int countDistinctIntegers(int[] nums) {
        Set<Integer> numsize = new HashSet<>();
        for (int i = 0; i< nums.length; i++){
            numsize.add(nums[i]);
            numsize.add(reverseNum(nums[i]));
        }
        return numsize.size();
    }
    public int reverseNum(int number){
        if (number / 10 == 0) return number;
        int digit = -1;
        int result = 0;
        int temp = number;
        while (temp > 0){
            digit ++;
            temp /= 10;
        }
        temp = number;
        while (digit >= 0){
            result += (temp % 10) * (Math.pow(10, digit));
            digit --;
            temp /= 10;
        }
        return result;
    }
}

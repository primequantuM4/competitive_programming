class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int leftptr = 0;
        int rightptr = 0;
        int oddNums = 0;
        int answer = 0;
        int tempCounter = 0;
        for (int i = 0; i < nums.length; i++){
           if (nums[i] % 2 != 0) {
               oddNums ++;
               tempCounter = 0;
           }
            rightptr ++;
            while (oddNums == k){
                if (nums[leftptr] % 2 != 0){
                    oddNums --;
                }
                leftptr ++;
                tempCounter ++;
            }
            answer += tempCounter;
        }
        return answer;
    }
}

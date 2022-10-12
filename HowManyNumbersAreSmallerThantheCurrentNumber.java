class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] res = new int[nums.length];
        int[] tempArr = nums.clone();
        Arrays.sort(tempArr);
        for (int i = 0; i< nums.length; i++){
            int curNum = nums[i];
            int count = 0;
            for (int j = 0; j < tempArr.length; j++){
                if (tempArr[j] < curNum){
                    count ++;
                }
                else{
                    res[i] = count;
                    break;
                } 
            }
        }
        return res;
    }
}

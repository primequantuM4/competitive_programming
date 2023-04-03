class Solution {
    public int[] findErrorNums(int[] nums) {
       Set<Integer> swapped = new HashSet<>();
        int index = 0;
        int[] repeatedNum = new int[2];

        while (index < nums.length){
            int correctedPosition = nums[index] - 1;
            if (correctedPosition != index && !swapped.contains(nums[index])){
                int temp = nums[index];
                nums[index] = nums[correctedPosition];
                nums[correctedPosition] = temp;
            }else{
                if (swapped.contains(nums[index]) && correctedPosition != index) repeatedNum[0] = nums[index];
                index++;
            }
            swapped.add(correctedPosition + 1);
        }
        for (int i = 0; i< nums.length; i++){
            if (nums[i] != i + 1) repeatedNum[1] = i + 1;
        }
        return repeatedNum;
        
    }
}

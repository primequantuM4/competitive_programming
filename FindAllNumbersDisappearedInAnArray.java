class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        //have a set and then do work
        Set<Integer> swapped = new HashSet<>();
        int index = 0;

        while (index < nums.length){
            int correctedPosition = nums[index] - 1;
            if (correctedPosition != index && !swapped.contains(nums[index])){
                int temp = nums[index];
                nums[index] = nums[correctedPosition];
                nums[correctedPosition] = temp;
            }else index++;
            swapped.add(correctedPosition + 1);
        }
        List<Integer> missingNums = new ArrayList<>();
        for (int i = 0; i< nums.length; i++){
            if (nums[i] != i + 1) missingNums.add(i + 1);
        }
        return missingNums;
    }
}

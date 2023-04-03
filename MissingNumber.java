class Solution {
    public int missingNumber(int[] nums) {
        //cyclic sort and then loop through the elements 
        //after sort whenever i!= nums[i] we return i
        // and if the loop finishes without returning return nums.length
        int index = 0;
        while (index < nums.length){
            if (nums[index] != index && nums[index] < nums.length){
                int temp = nums[index];
                int val = nums[temp];
                nums[temp] = nums[index];
                nums[index] = val;
            }else index ++;
        }
        for (int i = 0; i < nums.length; i++){
            if (nums[i] != i) return i;
        }
        return nums.length;
    }
}

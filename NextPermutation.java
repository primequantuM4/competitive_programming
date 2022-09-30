class Solution {
    public void nextPermutation(int[] nums) {
        int i = nums.length - 1;
        // This loop will help us identify the pivot element
        while (i > 0 && nums[i - 1] >= nums[i])
            i--;
        //This condition helps us for the extreme cases like 3 2 1 meaning we didn't find a pivot element
        if (i <= 0){
            int temp;
            for (int k = 0; k < nums.length / 2; k++) {
                temp = nums[k];
                nums[k] = nums[nums.length - k - 1];
                nums[nums.length - k - 1] = temp;
        }
            return;
        }
        int j = nums.length - 1;
        // here we are finding the element that is to be swapped with the pivot element
        while (nums[j] <= nums[i - 1])
            j--;
        //swapping occurs here
        int temp = nums[i - 1];
        nums[i - 1] = nums[j];
        nums[j] = temp;
        j = nums.length - 1;
        // we reverse the elements from i until the end of the array
        while (i < j) {
            temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
    }
}

class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        List<Integer> indicies = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == target) indicies.add(i);
            if(nums[i] > target) break; //will save us time from scanning all of the elements
        }
        return indicies;
    }
}

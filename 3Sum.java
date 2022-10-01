class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> list = new LinkedList();
        for (int i = 0; i < nums.length; i++){
            if (i == 0 || i > 0 && nums[i] != nums[i - 1]){
                int left = i + 1, right = nums.length - 1, sum = 0;
                while (left < right){
                    // System.out.println(sum + "left" + left + "right"+right);
                    sum = nums[i] + nums[left] + nums[right];
                    if (sum > 0) right --;
                    else if (sum < 0) left ++;
                    else {
                        list.add(Arrays.asList(nums[i], nums[left], nums[right]));
                        left ++;
                        while (nums[left] == nums[left - 1] && left < right) left ++;
                    }
                }
            }
        }
        return list;
    }
}

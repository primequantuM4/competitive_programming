class Solution {
    public int removeDuplicates(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int ptr = 0;
        for (int i: nums){
            if(!set.contains(i)){
                nums[ptr ++] = i;
            }
            set.add(i);
        }
        return ptr;
    }
}

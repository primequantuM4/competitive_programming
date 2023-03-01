class Solution {
    public int subarraySum(int[] nums, int k) {
        int subArrCount = 0;
        int sum = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);

        for (int i =0; i < nums.length; i++){
            sum += nums[i];

            subArrCount += map.getOrDefault(sum - k, 0);
            
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return subArrCount;
    }
}

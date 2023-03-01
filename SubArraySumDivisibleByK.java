class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        //try a prefix sum approach

        HashMap<Integer, Integer> map = new HashMap<>();
        int prefSum = 0;
        int subArrCount = 0;
        //edge case
        map.put(0,1);

        for (int i = 0; i < nums.length; i++){
            prefSum += nums[i];
            
            subArrCount += map.getOrDefault((prefSum % k + k) % k, 0);
    
            map.put((prefSum % k + k) % k, map.getOrDefault((prefSum % k + k) % k, 0) + 1);
        }

        return subArrCount;

    }
}

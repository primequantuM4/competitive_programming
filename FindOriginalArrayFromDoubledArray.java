class Solution {
    public int[] findOriginalArray(int[] changed) {
        if (changed.length % 2 != 0) return new int[] {};
        Arrays.sort(changed);
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < changed.length; i++){
            map.put(changed[i], map.getOrDefault(changed[i], 0) + 1);
        }
        int[] orignalArray = new int[changed.length / 2];
        int index = 0;
        for (int nums : changed){
            if (map.get(nums) > 0){
                map.put(nums, map.get(nums) - 1);
                int twiceNum = nums * 2;
                if (map.containsKey(twiceNum) && map.get(twiceNum) > 0){
                    map.put(twiceNum, map.get(twiceNum) - 1);
                    orignalArray[index++] = nums;
                }else {
                    return new int[] {};
                }
            }
        }
        return orignalArray;
    }
}

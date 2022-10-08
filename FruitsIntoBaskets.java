class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> map = new HashMap<>();
        int i;
        int left = 0;
        for (i = 0; i < fruits.length; i++){
            map.put(fruits[i], map.getOrDefault(fruits[i], 0) + 1);
            if (map.size() > 2){
                map.put(fruits[left], map.get(fruits[left]) - 1);
                if (map.get(fruits[left]) == 0) map.remove(fruits[left]);
                left ++;
            }
        }
        return i - left;
    }
}

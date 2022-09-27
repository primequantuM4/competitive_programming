class Solution {
    public List<Integer> partitionLabels(String s) {
        HashMap<Character, Integer> hashMap = new HashMap<Character, Integer>();
        char lastOccurence = s.charAt(s.length() - 1);
        hashMap.put(lastOccurence, s.length() - 1);
        List<Integer> list = new ArrayList<>();
        int size = 0;
        for (int i = s.length() - 2; i >= 0; i--){
            if (!hashMap.containsKey(s.charAt(i))){
                hashMap.put(s.charAt(i), i);
            }
        }
        int end = hashMap.get(s.charAt(0));
        for (int i = 0; i < s.length(); i++){
            int curr = hashMap.get(s.charAt(i));
            size ++;
            end = Math.max(end, curr);
            if (i == end){
                list.add(size);
                size = 0;
            }
            
        }
        
        return list;
    }
}

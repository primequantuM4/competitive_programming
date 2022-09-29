class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        HashSet<String> set = new HashSet<>();
        HashSet<String> set2 = new HashSet<>();
        for (int i = 0; i < s.length() - 9; i++){
            String sub = s.substring(i, i+ 10);
            if (set.contains(sub) && !set2.contains(sub)) set2.add(sub);
            set.add(sub);
        }
        return new ArrayList(set2);
    }
}

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        ArrayList<Integer> output = new ArrayList<>();
        int[] count = new int[26];
        for (char c: p.toCharArray()){
            count[c - 'a']++;
        }
        int left = 0;
        int right = 0;
        int total = p.length();
        
        while (right < s.length()){
            if (count[s.charAt(right++) - 'a']  -->= 1) total --;
            if (total == 0) output.add(left);
            if (right - left == p.length() && count[s.charAt(left++)- 'a']++ >= 0) total ++;
            
        }
        return output;
    }
}

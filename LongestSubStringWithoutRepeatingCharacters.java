class Solution {
    public int lengthOfLongestSubstring(String s) {
        int leftPointer = 0, rightPointer = 0, max = 0;
        HashSet<Character> set = new HashSet<>();
        while (rightPointer < s.length()){
            if (!set.contains(s.charAt(rightPointer))){
                set.add(s.charAt(rightPointer));
                rightPointer++;
            }else {
                max = Math.max(max, set.size());
                leftPointer ++;
                rightPointer = leftPointer;
                set.clear();
            }
        }
        max = Math.max(max, set.size());
        return max;
        
        
    }
}

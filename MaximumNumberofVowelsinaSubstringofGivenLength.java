class Solution {
    public int maxVowels(String s, int k) {
        int count = 0;
        for (int i = 0; i < k; i++){
               if (s.charAt(i) == 'a' || s.charAt(i) == 'e' || s.charAt(i) == 'i' || s.charAt(i) == 'o' || s.charAt(i) == 'u')
                   count ++;
           }
        int maxVow = count;
        int left = 0;
        int right = k -1;
        while (right < s.length() - 1){
            right ++;
            if (s.charAt(left) == 'a' || s.charAt(left) == 'e' || s.charAt(left) == 'i' || s.charAt(left) == 'o' || s.charAt(left) == 'u')
                   count --;  
            if (s.charAt(right) == 'a' || s.charAt(right) == 'e' || s.charAt(right) == 'i' || s.charAt(right) == 'o' || s.charAt(right) == 'u')
                   count ++;
            left ++;
            maxVow = Math.max(maxVow, count);
        }
        return maxVow;
    }
}

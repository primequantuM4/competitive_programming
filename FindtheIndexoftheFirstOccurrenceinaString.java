class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) return 0;
        if (needle.length() > haystack.length()) return -1;
        for (int i = 0; i < haystack.length() + 1 - needle.length(); i++){
            if (needle.charAt(0) == haystack.charAt(i)){
                int count = 0;
                 int j = 0;
                while (j < needle.length()){
                    if (needle.charAt(j) == haystack.charAt(j + i)){
                        count ++;
                    }
                    j ++;
                }
                if (count == needle.length()) return i;
            }
        }
        return -1;
    }
}

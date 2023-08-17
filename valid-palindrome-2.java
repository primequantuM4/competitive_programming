class Solution {
    public boolean isPalindrome(String s) {
        //first create a string that takes only a-z characters
        String compared = "";
        char[] c = s.toCharArray();
        for (char i : c){
            char lowerChar = Character.toLowerCase(i);
            if ((lowerChar >= 'a' && lowerChar <= 'z') || (i >= '0' && i <= '9')) compared += Character.toString(lowerChar);
        }
        // optimal solution is to use a two pointer approach and go to the middle this way we will have constant space
        c = compared.toCharArray();
        int left = 0;
        int right = c.length - 1;
        while (left < right){
            if (c[left ++] != c[right --]) return false;
        }
        return true;
    }
}
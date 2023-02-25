class Solution {
    public String removeDuplicateLetters(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        Stack<Character> stack = new Stack<>();
        HashSet<Character> set = new HashSet<>();
        for (int i = 0; i < s.length(); i++){
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }
        char[] chars = s.toCharArray();
        for (char c : chars){
            while (!stack.isEmpty() && stack.peek() > c && map.get(stack.peek()) >= 1 && !set.contains(c))
                set.remove(stack.pop());
            if (!set.contains(c)){
                stack.push(c);
                set.add(c);
            }
            map.put(c, map.get(c) - 1);
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) sb.append(stack.pop());
        return sb.reverse().toString();
        
        
    }
}

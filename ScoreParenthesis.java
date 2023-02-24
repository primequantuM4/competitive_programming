class Solution {
    public int scoreOfParentheses(String s) {
        char[] characters = s.toCharArray();
        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        int value = 0;
        for (char c: characters){
            if (c =='(') stack.push(0);

            else{
                int top = stack.pop();
                int depth = stack.pop();
                stack.push(depth + Math.max(2 * top, 1));
            }
        }
        return stack.pop();
    }
}

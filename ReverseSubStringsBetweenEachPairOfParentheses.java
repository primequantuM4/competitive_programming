class Solution {
    public String reverseParentheses(String s) {
        Stack<String> stack = new Stack<String>();
        Stack<String> rStack = new Stack<String>();
        String reversed = "";
        for (int i = 0; i < s.length(); i++){
            if (!(Character.toString(s.charAt(i)).equals(")"))){
                stack.push(Character.toString(s.charAt(i)));
            }else {
                while (!stack.peek().equals("(")){
                    reversed += stack.pop();
                    
                }
                stack.pop();
                for (int j = 0; j < reversed.length(); j++){
                    stack.push(Character.toString(reversed.charAt(j)));
                }
                reversed = "";
            }
            
        }
        while (!stack.empty()){
            rStack.push(stack.pop());
        }
        while (!rStack.empty()){
            reversed += rStack.pop();
        }
        return reversed;
    }
}

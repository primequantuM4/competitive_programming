class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Stack<Integer> stack = new Stack<>();
        int ptr = 0;
        for (int i = 0; i < pushed.length; i++){
            stack.push(pushed[i]);
            while(!stack.isEmpty() && stack.peek() == popped[ptr]){
                stack.pop();
                ptr ++;
            }
        }
        return stack.isEmpty();
        
    }
}

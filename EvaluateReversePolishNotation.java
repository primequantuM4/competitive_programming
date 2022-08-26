class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<Integer>();
        int firstNumber;
        int secondNumber;
        int result;
        for (String nums : tokens){
        	if (!(nums.equals("+") ||nums.equals("-") ||nums.equals("*") ||nums.equals("/")) ) {
        		stack.push(Integer.parseInt(nums));
        	}else if (nums.equals("+")) {
        		firstNumber = stack.pop();
        		secondNumber = stack.pop();
        		result = secondNumber + firstNumber;
        		stack.push(result);
        	}else if (nums.equals("-")) {
        		firstNumber = stack.pop();
        		secondNumber = stack.pop();
        		result = secondNumber - firstNumber;
        		stack.push(result);
        	}else if (nums.equals("*")) {
        		firstNumber = stack.pop();
        		secondNumber = stack.pop();
        		result = secondNumber * firstNumber;
        		stack.push(result);
        	}else if (nums.equals("/")) {
        		firstNumber = stack.pop();
        		secondNumber = stack.pop();
        		result = secondNumber / firstNumber;
        		stack.push(result);
        	}
        	
            
        }
        return stack.peek();
        
    }

}

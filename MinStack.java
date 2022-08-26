class MinStack {
	private Stack<Integer> stack = new Stack<Integer>();
	private Stack<Integer> stack2 = new Stack<Integer>();
    private int minNumber;
    private int prevMinNumber;
    public MinStack() {
        
    }
    
    public void push(int val) {
    	if (stack.empty() ) {
        	minNumber = val;
            stack2.push(minNumber);
        }
        stack.push(val);
        
        if (minNumber >= val) {
        	minNumber = val;
        	stack2.push(minNumber);
        }
    }
    
    public void pop() {
    	int poppedValue = stack.pop();
    	if (poppedValue == stack2.peek()) {
    		stack2.pop();
            minNumber = stack2.peek();
      }
    }
    
    public int top() {
    	return stack.peek();        
    }
    
    public int getMin() {
        return stack2.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */

class MyQueue {
	
    private Stack<Integer> stack = new Stack<Integer>();
	public MyQueue() {
		
	}
	 public void bottomInsert(int x){
		 if (stack.empty())
			 stack.push(x);
		 else {
			 int a = stack.peek();
			 stack.pop();
			 bottomInsert(x);
			 stack.push(a);
		 }
    }
	 
	public void reverse() {
		if (stack.size() > 0) {
			int x = stack.peek();
			stack.pop();
			reverse();
            bottomInsert(x);
			
			
		}
	}
    public void push(int x) {
        stack.push(x);
        
    }
    
    public int pop() {
    	reverse();
    	int poppedValue = stack.pop();
        reverse();
        return poppedValue;
    }
    
    public int peek() {
    	reverse();
    	int topValue = stack.peek();
    	reverse();
        return topValue;
    }
    
    public boolean empty() {
    	return stack.empty();
        
    }
}

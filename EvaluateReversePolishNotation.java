class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
		for (String expression: tokens){
			boolean notOperator = !(expression.equals("+") ||expression.equals("-") ||expression.equals("*") ||expression.equals("/"));

			if (notOperator) stack.push(Integer.parseInt(expression));
			else{
				int value = operate(stack.pop(), stack.pop(), expression);
				stack.push(value);
			}
		}
		return stack.pop();
    }
	public int operate(int nums1, int nums2, String operation){
		if (operation.equals("+")) return nums2 + nums1;
		else if (operation.equals("-")) return nums2 - nums1;
		else if (operation.equals("*")) return nums1 * nums2;
		else return nums2/ nums1;
	}
}

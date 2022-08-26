class Solution {
    public boolean isValid(String s) {
        Stack<String> stack = new Stack<String>();
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == '{' || s.charAt(i) == '(' || s.charAt(i) == '[') {
				stack.push(Character.toString(s.charAt(i)));
			}else if (s.charAt(i) == '}' || s.charAt(i) == ')' || s.charAt(i) == ']') {
				char comparedElement = s.charAt(i);
				if (stack.empty()) {
					return false;
				}
				String poppedElement = stack.pop();
				if (poppedElement.charAt(0) == '(' && comparedElement == ')') {
					continue;
				}else if (poppedElement.charAt(0) == '{' && comparedElement == '}') {
					continue;
				}else if (poppedElement.charAt(0) == '[' && comparedElement == ']') {
					continue;
				}else {
					return false;
				}
			}
			
		}
        if (!stack.empty()){
            return false;
        }
		return true;
    }
}

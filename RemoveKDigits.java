class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Integer> stack = new Stack<>();
        StringBuilder t = new StringBuilder();
        char[] ch = num.toCharArray();
        String temp = "";
        String res = "";
        int values;
        for (int i = 0; i < ch.length; i++){
            values = Character.getNumericValue(ch[i]);
            while (!stack.isEmpty() && stack.peek() > values && k > 0){
                stack.pop();
                k--;
            }
           stack.push(values);
        }
        while (k > 0){
            stack.pop();
                k--;
        }
        if (stack.isEmpty())
            return "0";
        while (!stack.isEmpty()){
            temp = Integer.toString(stack.pop());
            res += temp;
        }
        temp = "";
        t.append(res);
        t.reverse();
        res = t.toString();
        if (res.length() > 1){
            for (int i = 0; i < res.length(); i++) {
        	    if (temp.length() == 0) {
        		    if (res.charAt(i) != '0') {
        			    temp += Character.toString(res.charAt(i));
        		    }
        	    }else {
        		    temp += Character.toString(res.charAt(i));
        	    }
            }
            if (temp.length() == 0){
                return "0";
            }
            res = temp;
    }
        return res;
    }
}

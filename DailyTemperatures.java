class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        int[] answer = new int[temperatures.length];
        int currentIndex;
        int daysDifference;
        for (int i = 0; i < temperatures.length; i++){
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]){
                currentIndex = stack.pop();
                daysDifference = i - currentIndex;
                answer[currentIndex] = daysDifference;
            }
            stack.push(i);
        }
        while(!stack.isEmpty()){
            currentIndex = stack.pop();
            answer[currentIndex] = 0;
        }
        return answer;
        }
        
    }

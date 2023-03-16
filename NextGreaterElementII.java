class Solution {
    public int[] nextGreaterElements(int[] nums) {
        Stack<Integer> stack = new Stack<>();
        int[] greaterElements = new int[nums.length];
        Arrays.fill(greaterElements,-1);

        for (int i = 0; i < 2*nums.length; i++){
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i%nums.length]){
                int index = stack.pop() % nums.length;
                greaterElements[index] = nums[i%nums.length];
            }
            stack.push(i%nums.length);
        }
        return greaterElements;
    }
}

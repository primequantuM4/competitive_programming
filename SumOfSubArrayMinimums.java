class Solution {
    public int sumSubarrayMins(int[] arr) {
        // approach: find the minimum for all
        // what I know: it's guaranteed the total sum is added since the minimum of something is itself
        // what I don't know: how I'm going to keep track of the inner elements
        //try brute force first

        int minimumCount = 0;
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i <= arr.length; i++){

            while(!stack.isEmpty() && (i == arr.length || arr[stack.peek()] >= arr[i])){
                int value = stack.pop();
                int leftBoundary = stack.isEmpty()? -1: stack.peek();
                int rightBoundary = i;

                long count = (value - leftBoundary) * (rightBoundary  - value);
                minimumCount += (count * arr[value]) % 1000000007;
                minimumCount  %= 1000000007;
            }
            stack.push(i);
        }
        return minimumCount;
    }
}

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> dict = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        int manupilativeIdx;
        int[] res = new int[nums1.length];
        Arrays.fill(res, -1);
        for (int i = 0; i < nums1.length; i++){
            dict.put(nums1[i], i);
        }
        for (int i = 0; i < nums2.length; i++){
          while (!stack.isEmpty() && nums2[i] > stack.peek()){
              manupilativeIdx = dict.get(stack.pop());
              res[manupilativeIdx] = nums2[i];
          }
            if (dict.containsKey(nums2[i])){
                stack.push(nums2[i]);
            }

        }
        return res;
    }
}

class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int sum = 0;
        for (int i = 0; i < k; i++){
            sum += arr[i];
        }
   
        int count = (sum / k >= threshold)? 1 : 0;
        int left = 0;
        for (int i = k; i < arr.length; i++){
            left++;
            sum = sum - arr[left - 1] + arr[i];
            if (sum / k >= threshold) count ++;
        }
        return count;
    }
}

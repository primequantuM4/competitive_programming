class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int max = 0;
        while (left < right){
            if (height[right] > height[left]){
                max = Math.max((right - left) * height[left], max);
                left ++;
                
            }
            else{
                max = Math.max((right - left) * height[right], max);
                right --;
            } 
        }
        return max;
    }
}

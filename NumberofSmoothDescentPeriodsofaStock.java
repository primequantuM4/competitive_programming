class Solution {
    public long getDescentPeriods(int[] prices) {
        long res = 1;
        long left = 0;
        for (int right = 1;right < prices.length; right ++){
            if (prices[right - 1] - prices[right] == 1){
                long sum = right - left + 1;
                res += sum;
                
            }else{
                left = right;
                res ++;
            }
        }
        return res;
    }
}

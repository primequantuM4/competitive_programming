class Solution {
    public boolean judgeSquareSum(int c) {
        int number = c;
        for (long i = 0; i * i <= c; i++){
            double result = Math.sqrt(c- (i * i));
            if (result == (int)(result)) return true;
        }
        return false;
    }
}

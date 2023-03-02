class Solution {
    public double myPow(double x, int n) {
        //base case
        if (n == 0) return 1;

        //reccurence relation
        double half = myPow(x, n / 2);
        if (n % 2 == 0) return half * half;
        
        if (n > 0) return half * half * x;
        return half * half * (1/x);
    }
}

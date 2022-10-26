class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        int i = 0;
        long sum = 0;
        if (chalk.length == 1) return 0;
        for (int j = 0; j < chalk.length; j++){
            sum += (long) chalk[j];
        }
        long newK = (long) k % sum;
        while (newK - (long)chalk[i]>= 0){
            newK -= (long)chalk[i];
            i++;
        }
        return i;
    }
}

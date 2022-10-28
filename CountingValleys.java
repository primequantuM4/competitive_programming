class Result {

    /*
     * Complete the 'countingValleys' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER steps
     *  2. STRING path
     */
    public static int countingValleys(int steps, String path) {
    // Write your code here
        int altitude = 0;
        int valley = 0;
        for (int i = 0; i < path.length(); i++){
            if (path.charAt(i) == 'U') altitude ++;
            else{
                altitude --;
                if (altitude == -1) valley ++;
            }
        }
        return valley;
    }
}

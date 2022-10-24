class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] res = new int[n];
        Arrays.fill(res, 0);
        for (int i = 0; i < bookings.length; i++){
            int nums = bookings[i][1];
            for (int j = bookings[i][0] - 1; j < nums; j++){
                res[j] += bookings[i][2];
            }
        }
        return res;
    }
}

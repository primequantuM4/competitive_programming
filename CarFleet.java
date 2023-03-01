class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        Stack<Double> fleets = new Stack<>();
        int[][] pos = new int[position.length][2];

        //build the pos array
        for (int i =0; i < pos.length; i++){
            pos[i][0] = position[i];
            pos[i][1] = speed[i];
        }
        Arrays.sort(pos, (a, b) -> Integer.compare(a[0], b[0]));

        for (int i = pos.length - 1; i >= 0; i--){
            double topVal = !fleets.isEmpty()? fleets.peek(): 0;
            fleets.push((double)(target - pos[i][0]) / (double)pos[i][1]);

            if (fleets.size() > 1 && fleets.peek() <= topVal)
                fleets.pop();
        }
        return fleets.size();
    }
}

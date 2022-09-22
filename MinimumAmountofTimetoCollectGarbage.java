class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        //we have to change the travel to a prefix sum so that we can know individual truck time taken
        int[] totTravelTime = new int[travel.length];
        int sumCollected = 0;
        int glass =0;
        int paper = 0;
        int metal = 0;
        int ans = 0;
        totTravelTime[0] = travel[0];
        for(int i = 1; i < travel.length; i++){
            totTravelTime[i] = totTravelTime[i - 1] + travel[i];
        }
        for (int i = 0; i < garbage.length; i++){
            String current = garbage[i];
            ans += current.length();
            for(int j = 0; j < current.length();  j++){
                if (current.charAt(j) == 'M'){
                    metal = i;
                }else if (current.charAt(j) == 'P'){
                    paper = i;
                }else if (current.charAt(j) == 'G'){
                    glass = i;
                }
            }
            
        }
        // now we know the index of where the trucks will stop
        if (metal > 0) 
            sumCollected += totTravelTime[metal - 1]; 
        if (paper > 0) 
            sumCollected += totTravelTime[paper - 1]; 
        if (glass > 0) 
            sumCollected += totTravelTime[glass - 1]; 
        ans += sumCollected;
        return ans;
    }
}

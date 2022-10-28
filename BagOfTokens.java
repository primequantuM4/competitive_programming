class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);
        int l = 0;
        int r = tokens.length - 1;
        int score = 0;
        int maxGain = 0;
        while (l <= r){
            if (power >= tokens[l]){
                score ++;
                power -= tokens[l ++];
            }
            else if (score > 0 && power < tokens[l]){
                score --;
                power += tokens[r --];
            }else return 0;
            maxGain = Math.max(score, maxGain);
        }
        return maxGain;
    }
}

class Solution {
    public List<Integer> goodDaysToRobBank(int[] security, int time) {
        int[] dPref = new int[security.length];
        int[] iPref = new int[security.length];
        List<Integer> res = new ArrayList<>();
        dPref[0] = 0;
        iPref[security.length - 1] = 0;
        for (int i = 1; i < security.length - time; i++){
            if (security[i-1] < security[i]) dPref[i] = 0;
            else dPref[i] = dPref[i-1] + 1;
        }
        for (int i = security.length - 2; i>=time; i--){
            if (security[i + 1] < security[i]) iPref[i] = 0;
            else iPref[i] = iPref[i + 1] + 1;
        }
        for (int i = time; i < security.length - time; i++){
            if (iPref[i] >= time && dPref[i] >= time) res.add(i);
        }
        return res;
    }
}

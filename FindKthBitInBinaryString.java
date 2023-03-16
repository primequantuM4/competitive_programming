class Solution {
    public char findKthBit(int n, int k) {
        String builtBit = buildKBit(n);

        return builtBit.charAt(k-1);
    }
    public String buildKBit(int n){
        if (n == 1) return "0";

        String prev_bit = buildKBit(n-1);
        String cur_bit = prev_bit + "1" + invertAndReverse(prev_bit);

        return cur_bit;
    }

    public String invertAndReverse(String bit){
        StringBuilder sb = new StringBuilder();
        Map<Character, Character> map = new HashMap<>();
        map.put('0', '1');
        map.put('1', '0');

        for (int i = 0; i < bit.length(); i++){
            sb.append(Character.toString(map.get(bit.charAt(i))));
        }
        sb.reverse();
        return sb.toString();
    }
}

class Solution {
    public int findComplement(int num) {
        int bitOccupation = 0;
        int shiftedNum = num;

        while (shiftedNum != 0){
            shiftedNum >>= 1;
            bitOccupation++;
        }
        return num ^ ((1<<bitOccupation) - 1);
    }
}

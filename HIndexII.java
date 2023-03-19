class Solution {
    public int hIndex(int[] citations) {
        //binary search again
        if (citations.length == 1) return citations[0] >= 1? 1 : 0; 
        int low = 0;
        int length = citations.length;
        int high = citations.length - 1;
        int maxHIndexValue = 0;

        while (low <= high){
            int mid = low + (high - low) / 2;
            int hPapers = length - mid;
            if (citations[mid] == hPapers) return hPapers;
            
            if (citations[mid] < hPapers) low = mid + 1;
            else high = mid - 1;
        }

        return length - low;
    }
}

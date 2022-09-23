class Solution {
    public int maxScore(int[] cardPoints, int k) {
        // find the length of the sliding window
        int rightPointer = cardPoints.length - k - 1;
        int leftPointer = 0;
        System.out.println(cardPoints.length - k);
        int maxSum = 0;
        int currSum = 0;
        for (int i = rightPointer + 1; i < cardPoints.length; i++){
            maxSum += cardPoints[i];
        }
        currSum = maxSum;
        while (rightPointer < cardPoints.length - 1){
            rightPointer ++;
            currSum = currSum + cardPoints[leftPointer] - cardPoints[rightPointer];
            leftPointer ++;
            maxSum = Math.max(currSum, maxSum);
        }
        return maxSum;
        }
    }

class Solution {
    public int[] searchRange(int[] nums, int target) {
        //two times binary search
        int low = 0;
        int high = nums.length - 1;
        int start = -1, end = -1;

        while (low <= high){
            int mid = low + (high - low) / 2;

            if (nums[mid] > target) high = mid - 1;
            else if (nums[mid] < target) low = mid + 1;
            else{
                start = mid;
                high = mid - 1;
            }
        }
        low = 0; high = nums.length - 1;

        while (low <= high){
            int mid = low + (high - low) / 2;

            if (nums[mid] > target) high = mid - 1;
            else if (nums[mid] < target) low = mid + 1;
            else{
                end = mid;
                low = mid + 1;
            }
        }

        return new int[] {start, end};

    }
}

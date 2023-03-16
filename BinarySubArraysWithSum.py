class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        inner_window = defaultdict(int)
        inner_window[0] += 1

        subarray_count = 0
        pref_sum = 0
        
        for i in nums:
            pref_sum += i
            subarray_count += inner_window[pref_sum-goal]
            inner_window[pref_sum] += 1

        return subarray_count

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        #change it to 1 array
        # nums[i] <= nums[j] + diff provided i < j => nums[i] - nums[j] <= diff
        self.nums = []
        self.pairs = 0
        self.diff = diff
        for i in range(len(nums1)):
            self.nums.append(nums1[i] - nums2[i])
        print(self.mergeSort(0, len(self.nums) - 1))

        return self.pairs

    def mergeSort(self,left, right):
        if left == right:
            return [self.nums[left]]

        mid = left + (right - left) // 2
        left_half = self.mergeSort(left, mid)
        right_half = self.mergeSort(mid+1, right)

        self.checkDiffValidity(left_half, right_half)
        return self.merge(left_half, right_half)
    
    def checkDiffValidity(self, left_half, right_half):
        if left_half[0] - right_half[-1] > self.diff:
            return

        for num in left_half:
            insertion = len(right_half) - bisect_left(right_half, num - self.diff)
            self.pairs += insertion

        return

    def merge(self, left_half, right_half):
        left_ptr = 0
        right_ptr = 0
        result = []

        while left_ptr < len(left_half) and right_ptr < len(right_half):
            if left_half[left_ptr] < right_half[right_ptr]:
                result.append(left_half[left_ptr])
                left_ptr += 1

            else:
                result.append(right_half[right_ptr])
                right_ptr += 1

        result.extend(left_half[left_ptr:])
        result.extend(right_half[right_ptr:])

        return result


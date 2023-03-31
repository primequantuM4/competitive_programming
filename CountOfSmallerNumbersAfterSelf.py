class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.small_num = [0] * len(nums)
        self.modified_nums = []
        self.nums = nums
        for i in range(len(self.nums)):
            self.modified_nums.append((self.nums[i], i))
    
        dummy = self.divideArray(0, len(self.nums) - 1)
        return self.small_num


    def divideArray(self, left, right):
        if left == right:
            return [self.modified_nums[left]]
        mid = left + (right - left) // 2
        left_half = self.divideArray(left, mid)
        right_half = self.divideArray(mid+1, right)
        self.checkSmallerElements(left_half, right_half)
        return self.merge(left_half, right_half)
        
    def checkSmallerElements(self, left_half, right_half):
        for i in range(len(left_half)):
            if (left_half[i][0] < right_half[0][0]):
                continue
            low = 0
            high = len(right_half) - 1
            while (low <= high):
                mid = low + (high - low) // 2
                if left_half[i][0] > right_half[mid][0]:
                    low = mid + 1
                else:
                    high = mid - 1
            index = left_half[i][1]
            self.small_num[index] += low

    def merge(self, left_half, right_half):
        returned_array = []
        left_ptr = 0
        right_ptr = 0
        while left_ptr < len(left_half) and right_ptr < len(right_half):
            if left_half[left_ptr] > right_half[right_ptr]:
                returned_array.append(right_half[right_ptr]) 
                right_ptr += 1
            else:
                returned_array.append(left_half[left_ptr])
                left_ptr += 1

        while left_ptr < len(left_half) :
            returned_array.append(left_half[left_ptr])
            left_ptr += 1
        while right_ptr < len(right_half) :
            returned_array.append(right_half[right_ptr])
            right_ptr += 1
        return returned_array


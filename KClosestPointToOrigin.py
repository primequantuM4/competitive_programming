class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceLength = []
        for j in range(k):
            distanceLength.append(po[j])
        
        return distanceLength
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        pivot = len(nums) // 2
        left_list = self.merge_sort(nums[0:pivot])
        right_list = self.merge_sort(nums[pivot:])
        return self.merge(left_list, right_list)
    
    def merge(self, left_list, right_list):
        left_cursor, right_cursor = 0, 0
        ret = []
        while left_cursor < len(left_list) and right_cursor < len(right_list):
            if ((left_list[left_cursor][0] ** 2) + (left_list[left_cursor][1] ** 2)) ** 0.5 < ((right_list[right_cursor][0] ** 2) + (right_list[right_cursor][1] ** 2)) ** 0.5:
                ret.append(left_list[left_cursor])
                left_cursor += 1
            else:
                ret.append(right_list[right_cursor])
                right_cursor += 1
        ret.extend(left_list[left_cursor:])
        ret.extend(right_list[right_cursor:])
        
        return ret
        

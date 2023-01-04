class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n): nums1[i] = nums2[i]
            return
        insertion_idx = len(nums1) - 1
        ptr1 = m - 1
        ptr2 = n - 1

        while ptr1 >= 0 and ptr2 >= 0:
            if nums2[ptr2] >= nums1[ptr1]:
                nums1[insertion_idx] = nums2[ptr2]
                ptr2 -= 1
                insertion_idx -= 1
            else:
                nums1[ptr1], nums1[insertion_idx] = nums1[insertion_idx], nums1[ptr1]
                ptr1 -= 1
                insertion_idx -= 1
        while ptr2 >= 0:
            nums1[insertion_idx] = nums2[ptr2]
            insertion_idx -= 1
            ptr2 -= 1

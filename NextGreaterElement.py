class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1) 
        d = {val: idx for idx, val in enumerate(nums1)}

        for i in range(len(nums2)):
            n = nums2[i]
            if n in d:
                for j in range(i+1, len(nums2)):
                    if nums2[j] > n:
                        res[d[n]] = nums2[j]
                        break

        return res

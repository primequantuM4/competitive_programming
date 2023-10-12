# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        #find the mountain first
        def find_inc_target(lo, hi):
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if mountain_arr.get(mid) == target:
                    return mid
                elif mountain_arr.get(mid) > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1

        def find_dec_target(lo, hi):
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if mountain_arr.get(mid) == target:
                    return mid
                elif mountain_arr.get(mid) > target:
                    lo = mid + 1
                else:
                    hi = mid - 1
                
            return - 1

        lo, hi = 0, mountain_arr.length() - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        
        left = find_inc_target(0, hi)
        right = find_dec_target(hi, mountain_arr.length() - 1)

        if left == -1 or right == - 1:
            return max(left, right)
        return left
         
    

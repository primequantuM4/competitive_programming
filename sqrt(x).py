class Solution:
    def mySqrt(self, x: int) -> int:
        #implementation of binary search
        if x == 0:
            return 0

        low = 1
        high = x
        nearest = -1

        while low <= high:
            mid = low + (high - low) // 2

            if mid ** 2 > x:
                high = mid - 1
            elif mid ** 2 < x:
                if mid > nearest:
                    nearest = mid
                low = mid + 1

            else:
                return mid
            
        return nearest

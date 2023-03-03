# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        firstBad = n
        while low <= high:
            mid = low + (high - low) // 2
            versionBad = isBadVersion(mid)

            if versionBad:
                firstBad = min(mid, firstBad)
                high = mid - 1
            else:
                low = mid + 1

        return firstBad

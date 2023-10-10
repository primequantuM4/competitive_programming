class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        max_radius = 0
        for i in houses:
            left_heater, right_heater = self.binary_search(i, heaters)
            max_radius = max(max_radius, min(abs(i - heaters[left_heater]), abs(i - heaters[right_heater])))

        return max_radius


    def binary_search(self, target, heaters):
        hi, lo = len(heaters), -1

        while lo < hi - 1:
            mid = lo + (hi - lo) // 2

            if heaters[mid] > target:
                hi = mid
            else:
                lo = mid
        if lo == -1:
            lo = 0

        if hi == len(heaters):
            hi = len(heaters) - 1

        return lo, hi
        
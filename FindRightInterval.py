class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result = [-1] * len(intervals)

        for i in range(len(intervals)):
            intervals[i].append(i)

        intervals.sort()
        for start,end,index in sorted(intervals):
            low = 0
            high = len(intervals) - 1
            mimized_value = -1
            while low <= high:
                mid = low + (high - low) // 2

                if intervals[mid][0] < end:
                    low = mid + 1
                else:
                    mimized_value = intervals[mid][2]
                    high = mid - 1

            if mimized_value != -1:
                result[index] = mimized_value
        return result

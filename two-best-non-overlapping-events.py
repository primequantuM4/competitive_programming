class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()

        @cache
        def dp(idx, count):
            if count == 2 or idx >= len(events):
                return 0
            
            sr, er, val = events[idx]

            lo, hi = idx + 1, len(events) - 1

            while lo < hi:
                mid = (lo + hi) // 2
                if events[mid][0] <= er:
                    lo = mid + 1
                else: 
                    hi = mid
            
            if lo < len(events) and events[lo][0] > er:
                x = val + dp(lo, count + 1)
            else:
                x = val
            y = dp(idx + 1, count)

            return max(x, y)

        return dp(0, 0)

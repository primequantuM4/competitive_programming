class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds = 0
        ptr = 0
        while tickets[k]:
            if tickets[ptr]:
                tickets[ptr] -= 1
                seconds += 1
            ptr = (ptr + 1) % len(tickets)

        return seconds

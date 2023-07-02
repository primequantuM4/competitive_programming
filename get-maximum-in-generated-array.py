class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        self.max_num = 0

        @cache
        def findMin(num):
            if num == 0:
                return 0
            elif num == 1:
                return 1
            elif num == 2:
                return 1

            if num % 2 == 0:
                next_number = findMin(num // 2)
            else:
                next_number = findMin(num // 2) + findMin(num // 2 + 1)

            self.max_num = max(self.max_num, next_number)
            return next_number

        for i in range(n, -1, -1):
            self.max_num = max(findMin(i), self.max_num)
        return self.max_num

        
            
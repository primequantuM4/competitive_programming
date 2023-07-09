class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        product_answer = 1
        factors = set()
        for num in nums:
            if num == 2:
                factors.add(2)
                continue
            prod = int(math.sqrt(num))
            for i in range(2, prod + 1):
                if num % i == 0:
                    factors.add(i)
                    while num % i == 0:
                        num //= i
            if num > 2:
                factors.add(num)
        return len(factors)
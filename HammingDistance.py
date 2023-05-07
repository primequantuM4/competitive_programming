class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        converted_num = x ^ y

        while converted_num:
            if converted_num & 1 == 1:
                count += 1
            
            converted_num >>= 1

        return count

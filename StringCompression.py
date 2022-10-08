class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        res = []
        while left < len(chars):
            compared = left
            count = 0
            res.append(chars[left])
            for right in range(left, len(chars)):
                if chars[compared] != chars[right]:
                    break
                else:
                    left += 1
                    count += 1
            if count > 1 and count < 10:
                res.append(str(count))
            elif(count >= 10):
                nums = str(count)
                for i in range(len(nums)):
                    res.append(nums[i])
        while chars:
            chars.pop()
        for i in range(len(res)):
            chars.append(res[i])
        return len(chars)

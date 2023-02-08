class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #compare using strings
        #if they are equal in one instance check the len and sort it in that order

        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                value1, value2 = str(nums[j]), str(nums[j+1])
                for k in range(len(value1)):
                    if value1[k] < value2[k]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                    elif value1[k] == value2[k]:
                        isGreater = self.compare(value1, value2)
                        if isGreater:
                            nums[j], nums[j+1] = nums[j+1], nums[j]
                    break
        

        if nums[0] == 0 : return '0'
        return ''.join(map(str, nums))


    def compare(self, strX, strY):
        res1 = strX + strY
        res2 = strY + strX
        return res1 < res2
      
      
#Can be optimized and modularized will fix it when I have time

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heapify(nums)
        splitted_array = []

        while nums:
            cur_num = heappop(nums)
            i = len(splitted_array) - 1
            while i >= 0:
                if splitted_array[i][-1] == cur_num - 1:
                    break
                i-=1

            if i == -1:
                splitted_array.append([cur_num])
            else:
                splitted_array[i].append(cur_num) 

        for lists in splitted_array:
            if len(lists) < 3:
                return False

        return True

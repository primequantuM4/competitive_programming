class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def subs(idx,nums,N,lst,l):
            if idx>=N:
                val=0
                for i in lst:
                    val |= i
                l.append(val)
                return
            lst.append(nums[idx])
            subs(idx+1,nums,N,lst,l)
            lst.pop()
            subs(idx+1,nums,N,lst,l)
            return 
            
        lst=[]
        l=[]
        subs(0,nums,len(nums),lst,l)
        cnt=Counter(l)
        return max([i for i in cnt.values()])
            
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero=0
        prod=1

        for num in nums:
            if not num:
                zero+=1
                continue
            prod*=num
        
        if zero>1:
            return [0]*len(nums)
        res=[prod]*len(nums)

        if zero:
            for i in range(len(nums)):
                if nums[i]==0:
                    continue
                else:
                    res[i]=0
        else:
            for i in range(len(nums)):
                res[i]=res[i]//nums[i]
        
        return res

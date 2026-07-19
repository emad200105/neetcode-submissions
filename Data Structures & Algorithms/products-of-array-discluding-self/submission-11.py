class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero=0
        prod=1
        for num in nums:
            if num==0:
                zero+=1
            else:
                prod*=num
        
        if zero>1:
            return [0]*len(nums)
            
        if zero==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=prod
                else:
                    nums[i]=0
        else:
            for i in range(len(nums)):
                nums[i]=prod//nums[i]
        return nums
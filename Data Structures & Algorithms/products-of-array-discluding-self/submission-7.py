class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt=0
        prd=1
        for num in nums:
            if num==0:
                zero_cnt+=1
            else:
                prd*=num
        
        if zero_cnt>1:
            return [0]*len(nums)
        
        if zero_cnt==1:
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[i]=0
                else: nums[i]=prd
        else:
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=prd
                else:
                    nums[i]=prd//nums[i]
        return nums

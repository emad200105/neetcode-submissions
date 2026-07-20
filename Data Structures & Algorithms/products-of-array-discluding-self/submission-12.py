class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero=0
        prod=1

        for num in nums:
            if num==0:
                zero+=1
            else: prod*=num

        if zero>1:
            return [0]*len(nums)
        

        if zero:
            for index,value in enumerate(nums):
                if nums[index]==0:
                    nums[index]=prod
                else: nums[index]=0
        else:
            for index,value in enumerate(nums):
                nums[index]=prod//nums[index]
            
        return nums
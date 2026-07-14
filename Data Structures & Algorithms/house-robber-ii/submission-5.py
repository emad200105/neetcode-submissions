class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        res1=[0]*(len(nums))
        res2=[0]*(len(nums))

        res1[0]=nums[0]
        res1[1]=max(nums[0],nums[1])
        res2[1]=nums[1]
        res2[2]=max(nums[2],nums[1])

        for i in range(2,len(nums)-1):
            res1[i]=max(nums[i]+res1[i-2],res1[i-1])

        for i in range(3,len(nums)):
            res2[i]=max(nums[i]+res2[i-2],res2[i-1])
        
        return max(res1[len(nums)-2],res2[len(nums)-1])
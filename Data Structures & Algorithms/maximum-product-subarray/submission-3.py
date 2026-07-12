class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=[1]*len(nums)
        mini=[1]*len(nums)

        maxi[0]=nums[0]
        mini[0]=nums[0]

        for i in range(1,len(nums)):
            maxi[i]=max(nums[i],nums[i]*maxi[i-1],nums[i]*mini[i-1])
            mini[i]=min(nums[i],nums[i]*mini[i-1],nums[i]*maxi[i-1])

        return max(maxi)
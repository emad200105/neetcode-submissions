class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0]*len(nums)

        def sol(i):
            if i>=len(nums):
                return 0
            if dp[i]==0:
                dp[i]=max(nums[i]+sol(i+2),sol(i+1))
            return dp[i]
        return sol(0)
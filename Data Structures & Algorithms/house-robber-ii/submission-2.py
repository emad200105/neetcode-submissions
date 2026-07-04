class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1=[-1]*len(nums)
        dp2=[-1]*len(nums)

        def sol(i,range,dp):
            if i>=range:
                return 0
            if dp[i]==-1:
                dp[i]=max(nums[i]+sol(i+2,range,dp),sol(i+1,range,dp))
            return dp[i]
        
        
        

        return max(sol(0,len(nums)-1,dp1),sol(1,len(nums),dp2))
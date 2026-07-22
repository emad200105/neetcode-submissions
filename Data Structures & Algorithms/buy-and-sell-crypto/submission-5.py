class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        maxi=0
        mini=nums[0]

        for num in nums:
            maxi=max(maxi,num-mini)
            mini=min(mini,num)
        return maxi
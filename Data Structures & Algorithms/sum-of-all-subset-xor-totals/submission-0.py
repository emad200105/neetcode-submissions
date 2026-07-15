class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        maxi=0

        def sol(i,sumi):
            nonlocal maxi
            if i>=len(nums):
                maxi+=sumi
                return
            
            sol(i+1,sumi^nums[i])
            sol(i+1,sumi)

        sol(0,0)
        return maxi
            
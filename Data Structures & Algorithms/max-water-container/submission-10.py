class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1


        maxi=0

        while l<r:
            height=min(nums[l],nums[r])
            width=r-l

            maxi=max(maxi,height*width)

            if nums[l]<nums[r]:
                l+=1
            else: r-=1
        return maxi
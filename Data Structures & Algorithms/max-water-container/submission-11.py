class Solution:
    def maxArea(self, nums: List[int]) -> int:
        maxi=0

        i,j=0,len(nums)-1

        while i<j:
            height=min(nums[i],nums[j])
            width=j-i
            area=height*width

            maxi=max(maxi,area)

            if nums[i]>nums[j]:
                j-=1
            else:
                i+=1
        return maxi
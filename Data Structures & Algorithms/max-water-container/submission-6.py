class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxi=0

        while(l<r):
            curr=min(heights[l],heights[r])
            area=curr*(r-l)
            maxi=max(maxi,area)

            if heights[l]>heights[r]:
                r-=1
            else: l+=1
        return maxi

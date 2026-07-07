class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k=len(nums)-1
        i=0
        j=0
        while j<=k:
            if nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            elif nums[j]==2:
                nums[j],nums[k]=nums[k],nums[j]
                k-=1
                j-=1

            j+=1

        
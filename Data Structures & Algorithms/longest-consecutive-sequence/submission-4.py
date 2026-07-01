class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)

        maxi=0
        for num in nums:
            cnt=0
            while num in st:
                cnt+=1
                num+=1
            maxi=max(cnt,maxi)
        return maxi
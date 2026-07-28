class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)

        maxi=0

        for num in nums:
            cnt=0

            if num-1 not in nums:
                cur=num

                while cur in nums:
                    cnt+=1
                    cur+=1
            maxi=max(cnt,maxi)
        return maxi
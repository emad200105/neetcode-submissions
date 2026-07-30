import heapq

class Solution:
    def lastStoneWeight(self, nums: List[int]) -> int:
        nums=[-i for i in nums]
        heapq.heapify(nums)

        while len(nums)>1:
            it=heapq.heappop(nums)
            it2=heapq.heappop(nums)
            res=it-it2
            if res==0:
                continue
            heapq.heappush(nums,res)
        
        if nums:
            return -nums[0]
        return 0

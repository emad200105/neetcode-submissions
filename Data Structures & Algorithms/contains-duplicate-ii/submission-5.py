class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dt=dict()

        for i,v in enumerate(nums):
            if v in dt:
                if i-dt[v]<=k:
                    return True
            dt[v]=i
        return False
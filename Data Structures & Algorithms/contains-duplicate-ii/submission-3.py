class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dt=dict()

        for index,value in enumerate(nums):
            if value in dt:
                if index-dt[value]<=k:
                    return True
            dt[value]=index
        return False
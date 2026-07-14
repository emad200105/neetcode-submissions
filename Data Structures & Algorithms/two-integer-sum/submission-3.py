class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt={}

        for index,val in enumerate(nums):
            rem=target-val

            if rem in dt:
                return [dt[rem],index]
            else:
                dt[val]=index
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt=dict()

        for index,value in enumerate(nums):
            rem=target-value

            if rem in dt:
                return [dt[rem],index]
            else:
                dt[value]=index
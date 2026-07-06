class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n,(n+n)):
            nums.append(nums[i-n])
        return nums
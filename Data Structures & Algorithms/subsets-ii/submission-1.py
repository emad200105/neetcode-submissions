class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        def sol(i,arr):
            if i==len(nums):
                res.append(arr.copy())
                return
            arr.append(nums[i])
            sol(i+1,arr)
            arr.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            sol(i+1,arr)
        sol(0,[])
        return res

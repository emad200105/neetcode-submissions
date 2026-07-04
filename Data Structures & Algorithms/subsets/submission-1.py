class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def sol(i,arr):
            if i==len(nums):
                res.append(arr.copy())
                return
            arr.append(nums[i])
            sol(i+1,arr)
            arr.pop()
            sol(i+1,arr)

        sol(0,[])
        return res
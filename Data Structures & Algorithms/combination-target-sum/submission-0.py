class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def sol(sum,i,arr):
            if i==len(nums) or sum>target:
                return
            if sum==target:
                res.append(arr.copy())
                return
            arr.append(nums[i])
            sol(sum+nums[i],i,arr)
            arr.pop()
            sol(sum,i+1,arr)

        sol(0,0,[])
        return res
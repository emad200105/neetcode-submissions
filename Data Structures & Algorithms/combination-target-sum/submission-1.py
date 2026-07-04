class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def sol(i,sum,arr):
            if i==len(nums) or sum>target:
                return
            if sum==target:
                res.append(arr.copy())
                return
            
            arr.append(nums[i])
            sol(i,sum+nums[i],arr)
            arr.pop()
            sol(i+1,sum,arr)

        sol(0,0,[])
        return res
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def insert(i,arr):
            if(i==len(nums)):
                return res.append(arr.copy())

            arr.append(nums[i])
            insert(i+1,arr)
            arr.pop()
            insert(i+1,arr)
        
        insert(0,[])
        return res

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dt={}
        for num in nums:
            if num in dt:
                dt[num]+=1
            else:
                dt[num]=1
        n=len(nums)//3
        res=[]
        for d in dt:
            if dt[d]>n:
                res.append(d)
        return res
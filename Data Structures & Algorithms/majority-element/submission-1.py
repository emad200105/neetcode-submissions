class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dt={}
        for num in nums:
            if num in dt:
                dt[num]+=1
            else:
                dt[num]=1
        res=sorted(dt.keys(),key=lambda x: dt[x],reverse=True)
        return res[0]
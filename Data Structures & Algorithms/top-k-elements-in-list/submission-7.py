class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt={}

        for num in nums:
            if num in dt:
                dt[num]+=1
            else:
                dt[num]=1
        
        res=dict(sorted(dt.items(),key=lambda x: x[1], reverse=True))

        return list(res.keys())[:k]
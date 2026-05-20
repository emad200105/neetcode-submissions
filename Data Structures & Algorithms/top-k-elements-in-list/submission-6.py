class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt=dict()

        for num in nums:
            if num in dt:
                dt[num]+=1
            else:
                dt[num]=0
        
        dt=sorted(dt.items(),key=lambda x: x[1],reverse=True)
        result=[]

        for i in range(k):
            result.append(dt[i][0])

        return result
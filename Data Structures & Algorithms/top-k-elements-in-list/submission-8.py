class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt=defaultdict(int)

        for num in nums:
            dt[num]+=1
        
        return list(sorted(dt.keys(),key=lambda x: dt[x],reverse=True))[:k]
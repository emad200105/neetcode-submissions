class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dt=defaultdict(int)

        for num in nums:
            dt[num]+=1
        
        return list(sorted(dt.keys(),key=lambda x: dt[x]))[-1]
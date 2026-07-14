class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dt=defaultdict(int)

        for num in nums:
            dt[num]+=1
        
        return sorted(dt,key=lambda x: dt[x],reverse=True)[0]
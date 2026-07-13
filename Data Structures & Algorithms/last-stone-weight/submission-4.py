import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)


        while len(stones) >1:
            num1=heapq.heappop(stones)
            num2=heapq.heappop(stones)
            res=num1-num2
            if res:
                heapq.heappush(stones,res)
        if stones:
            return -heapq.heappop(stones)
        return 0
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-x for x in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            num1=heapq.heappop(stones)
            num2=heapq.heappop(stones)
            heapq.heappush(stones,num1-num2)
        return -heapq.heappop(stones)
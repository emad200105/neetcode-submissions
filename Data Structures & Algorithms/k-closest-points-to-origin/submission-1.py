import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]

        for x,y in points:
            distance=math.sqrt(math.pow(x,2)+math.pow(y,2))
            heapq.heappush(res,(distance,[x,y]))
        
        res2=[]

        for i in range(k):
            res2.append(heapq.heappop(res)[1])

        return res2
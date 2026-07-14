import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for point in points:
            distance=math.sqrt(math.pow(point[0],2)+math.pow(point[1],2))
            heapq.heappush(heap,(distance,point))
        
        res=[]

        while k:
            res.append(heapq.heappop(heap)[1])
            k-=1
        return res
            

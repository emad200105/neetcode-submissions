import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=[-i for i in nums]
        heapq.heapify(self.nums)
        self.k=k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,-val)
        back=[]

        for i in range(self.k):
            back.append(heapq.heappop(self.nums))
        
        res=back[-1]

        while back:
            heapq.heappush(self.nums,back.pop())

        return -res

        

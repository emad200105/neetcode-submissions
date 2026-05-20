class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minNum=float('inf')

        for price in prices:
            maxp=max(maxp,price-minNum)
            minNum=min(minNum,price)

        return maxp
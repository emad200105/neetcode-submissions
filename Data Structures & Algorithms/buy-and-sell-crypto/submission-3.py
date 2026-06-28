class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        
        maxi=0
        mini=prices[0]

        for price in prices:
            maxi=max(maxi,price-mini)
            mini=min(mini,price)
        return maxi
class Solution(object):
    def maxPriceProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=prices[0]
        maxProfit=0

        for sell in prices:
            maxProfit=max(maxProfit,sell-buy)
            buy=min(sell,buy)
        
        return maxProfit
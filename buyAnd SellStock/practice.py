class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest=prices[0]
        maxProfit=0
        for price in prices:
            if(price<=lowest):
                lowest=price
                continue
            if(price-lowest>maxProfit):
                maxProfit=price-lowest
        
        return maxProfit


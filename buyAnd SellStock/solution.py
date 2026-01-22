class Solution(object):
    def maxPriceProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice=max(prices)+1
        maxPrice=0
        profit=0
        for price in prices:
            if(price<minPrice):
                minPrice=price
                maxPrice=0
                continue
            if(price>maxPrice):
                maxPrice=price
            if(maxPrice-minPrice>profit):
                profit=maxPrice-minPrice
        return profit
    
sol=Solution()
print(sol.maxPriceProfit([7,1,5,3,6,4]))

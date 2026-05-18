class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        memo={}
        def dfs(i,buy):
            if(i>=len(prices)):
                return 0
            if(i,buy) in memo:
                return memo[(i,buy)]
            coolDown=dfs(i+1,buy)
            if(buy):
                result = max(dfs(i+1,not buy) - prices[i],coolDown)
            else:
                result=max(dfs(i+2,not buy) + prices[i],coolDown)
            memo[(i,buy)]=result
            return result
        return dfs(0,True )
                    
            
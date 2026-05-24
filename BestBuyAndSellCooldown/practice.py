class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        memo={}
        def dfs(buy,i):
            if(i>=len(prices)):
                return 0
            if((buy,i) in memo):
                return memo[(buy,i)]
            if(buy):
                memo[(buy,i)]=max(dfs(not buy,i+1)-prices[i],dfs(buy,i+1))
            else:
                memo[(buy,i)]=max(dfs(True,i+2)+prices[i],dfs(False,i+1))
            return memo[(buy,i)]
        return dfs(True,0)

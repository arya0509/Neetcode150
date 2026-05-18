class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo={}
        def dfs(a,i):
            if(a==0):
                return 1
            if(i==len(coins) or a<0):
                return float("inf")
            if (a,i) not in memo:
                res= min(1+dfs(a-coins[i],i),dfs(a,i+1))
                memo([a,i])=res
            return memo([a,i])
        res= dfs(amount,0)
        return res if res!=float("inf") else -1 
            
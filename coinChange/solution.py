class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.cache={}
        
        def dfs(total):
            if(total==0):
                return 0
            res=float('inf')
            for i in range(len(coins)):
                if(self.cache.get(total-coins[i],False)):
                    res=min(res,self.cache[total-coins[i]])
                    continue
                if(total-coins[i]>=0):
                 ans=1+dfs(total-coins[i])
                 res=min(res,ans)
                 self.cache[total-coins[i]]=ans
            return res 
        res=dfs(amount)
        return res if res!=float("inf") else -1


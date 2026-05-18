class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        memo={}
        def dfs(a,i):
            if(a==0):
                return 1
            if(i==len(coins)):
                return 0
            if((a,i) in memo):
                return memo[(a,i)]
            if(a>=coins[i]):
                memo[(a,i)]=dfs(a,i+1)+dfs(a-coins[i],i)
                return memo[(a,i)]
            return 0
        return dfs(amount,0)

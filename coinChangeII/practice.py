class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        memo={}
        def dfs(i,curr):
            if(curr==amount):
                return 1
            if(curr>amount or i==len(coins)):
                return 0
            if((curr,i) in memo):
                return memo[(curr,i)]
            memo[(curr,i)]=dfs(i,curr+coins[i]) +dfs(i+1,curr)
            return memo[(curr,i)]
        return dfs(0,0)
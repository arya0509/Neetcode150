class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if(s==t):
            return 1
        if(len(s)<len(t)):
            return 0
        memo={}
        def dfs(i,j):
            if(j==len(t)):
                return 1
            if(i==len(s)):
                return 0
            if((i,j) in memo):
                return memo[(i,j)]
            res=dfs(i+1,j)
            if(s[i]==t[j]):
                res+=dfs(i+1,j+1)
            memo[(i,j)]=res
            return res 
        return dfs(0,0)
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        memo={}
        if(len(s)<len(t)):
            return 0
        def dfs(i,j):
            if(i==len(s) or j==len(t)):
                return 0
            if ((i,j) in memo):
                return memo[(i,j)]
            res=dfs(i+1,j)
            if(s[i]==t[j]):
                if(j+1==len(t)):
                    res+=1
                else:
                    res+=dfs(i+1,j+1)
            memo[(i,j)]=res
            return memo[(i,j)]
        return dfs(0,0)
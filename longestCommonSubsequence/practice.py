class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        memo={}
        def dfs(i,j):
            if(i==len(text1) or j==len(text2)):
                return 0
            if((i,j) in memo):
                return memo[(i,j)]
            if(text1[i]==text2[j]):
                memo[(i,j)]=1+dfs(i+1,j+1)
            else:
                memo[(i,j)]=max(dfs(i+1,j),dfs(i,j+1))
            return memo[(i,j)]
        dfs(0,0)
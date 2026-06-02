class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2:a str
        :rtype: int
        """
        memo={}
        def dfs(i,j):
            if ((i,j) in memo):
                return memo[(i,j)]
            if(i==len(word1)):
                if(j==len(word2)):
                    return 0
                memo[(i,j)]=1+dfs(i,j+1)
                return memo[(i,j)]
            if(j==len(word2)):
                memo[(i,j)]=1+dfs(i+1,j)
                return memo[(i,j)]
            elif(word1[i]==word2[j]):
                memo[(i,j)]=dfs(i+1,j+1)
            else:
                memo[(i,j)]=1+min(dfs(i+1,j+1),dfs(i+1,j),dfs(i,j+1))
            return memo[(i,j)]
        return dfs(0,0)
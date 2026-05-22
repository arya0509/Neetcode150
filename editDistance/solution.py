class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if(word1==word2):
            return 0 
        cache={}
        def dfs(i,j):
            if(i,j) in cache:
                return cache[(i,j)]
            if(i==len(word1) or j==len(word2)):
                if(i!=len(word1)):
                    cache[(i,j)]= 1+dfs(i+1,j)
                elif(j!=len(word2)):
                    cache[(i,j)]= 1+dfs(i,j+1)
                else:
                    cache[(i,j)]=0
                return cache[(i,j)]
            if(word1[i]==word2[j]):
                cache[(i,j)]=dfs(i+1,j+1)
            else:
                cache[(i,j)]=min(1+dfs(i+1,j+1),1+dfs(i+1,j),1+dfs(i,j+1))
            return cache[(i,j)]
        return dfs(0,0)
             
            
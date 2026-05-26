class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        memo={}
        def dfs(i,j,k):
            if(i==len(s1) and j==len(s2)):
                if (k==len(s3)):
                    return True 
                return False 
            if (i,j) in memo:
                return memo[(i,j)] 
            elif (i<len(s1) and j<len(s2) and k<len(s3) and s1[i]==s2[j]==s3[k]):
                memo[(i,j)]=dfs(i+1,j,k+1) or dfs(i,j+1,k+1)
            elif(i<len(s1) and k<len(s3) and s1[i]==s3[k]):
                memo[(i,j)]=dfs(i+1,j,k+1)
            elif(j<len(s2) and k<len(s3) and s2[j]==s3[k]):
                memo[(i,j)]=dfs(i,j+1,k+1)
            else:
                memo[(i,j)]=False
            return memo[(i,j)]
        return dfs(0,0,0)
            
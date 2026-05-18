class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        memo={}
        def dfs(i1,i2,i3):
            if(i3==len(s3) and i1==len(s1) and i2==len(s2)):
                return True 
            res=False if (i1,i2) not in memo else memo[(i1,i2)]
            if(i1<len(s1) and i2<len(s2) and s3[i3]==s2[i2] and s3[i3]==s1[i1]):
                if((i1,i2) not in memo):
                    res=dfs(i1,i2+1,i3+1) or dfs(i1+1,i2,i3+1)
                    memo[(i1,i2)]=res
            elif(i1<len(s1) and i3<len(s3) and s3[i3]==s1[i1]):
                if((i1,i2) not in memo):
                    res=dfs(i1+1,i2,i3+1)
                    memo[(i1,i2)]=res
            elif(i2<len(s2) and i3<len(s3) and s3[i3]==s2[i2]):
                if((i1,i2) not in memo):
                    res=dfs(i1,i2+1,i3+1)
                    memo[(i1,i2)]=res
            
            return res 
        return dfs(0,0,0)
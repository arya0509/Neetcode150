class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo={}
        def dfs(st,i):
            if(i==len(s)):
                return 1
            if(s[i]=="0" and st==""):
                return 0
            res=0
            if(int(st+s[i])<27):
                if(int(st+s[i])>9):
                    res+=dfs("",i+1)
                else:
                    if(not memo[i]):
                        res=dfs("",i+1)+dfs(s[i],i+1)
                        memo[i]=res
                    return memo[i]
            return res 
        return dfs("",0)

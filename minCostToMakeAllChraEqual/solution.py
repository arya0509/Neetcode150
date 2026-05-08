class Solution(object):
    def minimumCost(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        n=len(s)
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                continue
            res+=min(i,n-i)
        return res 

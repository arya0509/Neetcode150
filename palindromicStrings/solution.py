class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0

        for i in range(len(s)):
            c+=1
            l=i-1
            r=i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                c+=1
                l-=1
                r+=1
            l=i
            r=i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                c+=1
                l-=1
                r+=1
        return c
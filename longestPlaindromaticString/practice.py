class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(len(s)==0):
            return s
        maxLen=1
        ans=s[0]
        for i in range(len(s)):
            l=i-1
            r=i+1

            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(r-l+1>maxLen):
                    maxLen=r-l+1
                    ans=s[l:r+1]
                l-=1
                r+=1
            l=i
            r=i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(r-l+1>maxLen):
                    maxLen=r-l+1
                    ans=s[l:r+1]
                l-=1
                r+=1
        return ans
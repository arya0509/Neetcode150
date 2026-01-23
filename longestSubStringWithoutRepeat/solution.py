class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        r=0
        maxLength=0
        subString=set()
        while(r!=len(s)):
            
            while(s[r] in subString):
                subString.remove(s[l])
                l+=1    
                

            subString.add(s[r])
            if(r-l+1>maxLength):
                maxLength=r-l+1
            r+=1


        return maxLength
sol=Solution()
print(sol.lengthOfLongestSubstring("bbbbb"))
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique=[]
        maxLen=1
        l=0
        for r in range(len(s)):
            if(unique and s[r] in unique):
                while(s[r] in unique):
                    unique.remove(s[l])
                    l+=1
            unique.append(s[r])
            print(unique)
            maxLen=max(maxLen,r-l+1)
        return maxLen
    
sol=Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        index=0
        maxLen=1
        for i in range(len(s)):
            left=i-1
            right=i+1

            while(left>=0 and right < len(s)):
                if(s[left]!=s[right]):
                    break
                if(right-left+1>maxLen):
                    index=left
                    maxLen=right-left+1
                left-=1
                right+=1
            left=i
            right=i+1
           
            while(left>=0 and right < len(s)):
                if(s[left]!=s[right]):
                    break
                if(right-left+1>maxLen):
                    index=left
                    maxLen=right-left+1
                left-=1
                right+=1
       
        return s[index:index+maxLen]
            
        


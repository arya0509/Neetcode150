class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        end=len(s)-1
        start=0
        while(start<end):
            while(end!=start and not s[start].isalnum()):
                start+=1
                
            while(end!=start and not s[end].isalnum()):
                end-=1
                
            if(s[start].lower()!=s[end].lower()):
                return False  
            start+=1
            end-=1
        
        return True

sol=Solution()
print(sol.isPalindrome("a,,a"))
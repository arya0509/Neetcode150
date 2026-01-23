from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l=0
        maxF=0
        res=0
        count=defaultdict(int)
        for r in range(len(s)):
            count[s[r]]+=1
            maxF=max(maxF,count[s[r]])

            while (r-l+1) -maxF>k:
                count[s[l]]-=1
                l+=1
            
            res=max(res,r-l+1)
        
        return res
                
sol=Solution()
print(sol.characterReplacement("ABBB",2))
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l=0
        maxLen=0
        freq={}
        mostFreqChar=0
        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1
            mostFreqChar=max(mostFreqChar,freq[s[r]])
            if(freq):
                if(r-l+1)-mostFreqChar<=k:
                    maxLen=max(maxLen,r-l+1)
                else:
                    while((r-l+1)-mostFreqChar>k):
                        freq[s[l]]-=1
                        l+=1
            
        return maxLen
    

sol=Solution()
print(sol.characterReplacement("AABABBA",1))
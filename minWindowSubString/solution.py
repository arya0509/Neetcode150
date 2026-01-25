from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t=="":
            return ""
        
        minLen=float("infinity")
        tDict={}
        window={}
        for c in t:
            tDict[c]=1+tDict.get(c,0)
        have,need=0,len(tDict)

        l=0
        res=[-1,-1]
        for r in range(len(s)):
            c=s[r]
            
            window[c]=1+window.get(c,0)
            
            if(c in tDict and window[c]==tDict[c]):
                have+=1
            
            while(need==have):
                if(r-l+1<minLen):
                    minLen=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                
                
                if(s[l] in tDict and window[s[l]]<tDict[s[l]]):
                    have-=1
                l+=1
        l,r=res
         
        return s[l : r + 1] if minLen != float("infinity") else ""
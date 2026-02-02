class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sDict={}
        tDict={}
        for i in t:
            tDict[i]=tDict.get(i,0)+1
            sDict[i]=0

        minLen=len(s)+1
        window=[0,0]
        match=0
        l=0
        for r in range(len(s)):
           
            if s[r] in sDict:
                sDict[s[r]]=sDict.get(s[r],0)+1
                if(sDict[s[r]]<=tDict[s[r]]):
                    match+=1
            while(match==len(t) and l<=r):
                if(r-l+1<minLen):
                    minLen=r-l+1
                    window=[l,r]
                if(s[l] in sDict):
                    if(sDict[s[l]]==tDict[s[l]]):
                        match-=1
                    sDict[s[l]]-=1
                l+=1
        if(minLen==len(s)+1):
            return ""
        return s[window[0]:window[1]+1]
sol=Solution()
print(sol.minWindow("a",'a'))

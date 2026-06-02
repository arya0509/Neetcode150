class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res=[]
        freq={}
        for i in range(len(s)-1,-1,-1):
            if(s[i] not in freq):
                freq[s[i]]=i

        i=0
        while(i<len(s)):
            end=freq[s[i]]
            curr=0
            while(i<end+1):
                curr+=1
                end=max(end,freq[s[i]])
                i+=1
            res.append(curr)
            curr=0
        return res 
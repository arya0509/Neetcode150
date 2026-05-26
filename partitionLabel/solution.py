from collections import Counter
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last={}
        for i in range(len(s),-1,-1):
            if(s[i] not in last):
                last[s[i]]=i
        arr=[]
        size=0
        maxLast=last[s[0]]
        for i in range(len(s)):
            maxLast=max(maxLast,last[s[i]])
            size+=1
            if(i==maxLast):
                arr.append(size)
                size=0
                maxLast=-1
        return arr
            

        
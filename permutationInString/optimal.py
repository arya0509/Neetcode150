class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if(len(s2)<len(s1)):
            return False
        
        s1List=[0] * 26
        s2List=[0] * 26
        
        for i in range(len(s1)):
            s1List[ord(s1[i]) - ord('a')]+=1
            s2List[ord(s2[i]) - ord('a')]+=1
        
        matches=0

        for i in range(26):
            if(s1List[i]==s2List[i]):
                matches+=1
        l=0
        for r in range(len(s1),len(s2)):
            if(matches==26):
                return True 
            index=ord(s2[r]) - ord('a')
            s2List[index]+=1

            if(s2List[index]==s1List[index]):
                matches+=1
            elif(s2List[index]==s1List[index]+1):
                matches-=1

            
            index=ord(s2[l]) - ord('a')
            s2List[index]-=1

            if(s2List[index]==s1List[index]):
                matches+=1
            elif(s2List[index]==s1List[index]-1):
                matches-=1
            l+=1
        return matches==26
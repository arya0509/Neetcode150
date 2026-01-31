class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        frequencyS1=[0] * 26 
        frequencyS2=[0] * 26 
        for i in range(len(s1)):
            frequencyS1[ord(s1[i])-ord('a')]+=1
        l=0
        for r in range(len(s2)):
            frequencyS2[ord(s2[r])-ord('a')]+=1
            # print(f"S1: {frequencyS1}   S2:{frequencyS2}")
            if frequencyS1==frequencyS2 and r!=0:                
                return True            
            
            if(r-l+1>=len(s1)):
                frequencyS2[ord(s2[l])-ord('a')]-=1
                l+=1
        

        return False
    
sol=Solution()
print(sol.checkInclusion("adc","dcda"))
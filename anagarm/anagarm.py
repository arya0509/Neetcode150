class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t)!=len(s):
            return False
        word_dictionary=dict()
        for i in s:
            if(word_dictionary.get(i)!=None):
                word_dictionary[i]=word_dictionary.get(i)+1
                continue
            word_dictionary[i]=1

        
        for i in t:
            if(word_dictionary.get(i)!=0 and word_dictionary.get(i)!=None ):
                word_dictionary[i]=word_dictionary.get(i)-1
                continue
            return False
        return True
            

sol = Solution()
print(sol.isAnagram(s="rat",t="car"))
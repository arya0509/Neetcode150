from collections import Counter 
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open=[]
        star=[]
        for c in range(len(s)):
            if(s[c]=="("):
                open.append(c)
            elif(s[c]=="*"):
                star.append(c)
            else:
                if(open):
                    open.pop()
                elif(star):
                    star.pop()
                else:
                    return False
                
        while(open and star):
                o=open.pop()
                s=star.pop()
                if(o>s):
                    return False
                  
                
        return len(open)==0
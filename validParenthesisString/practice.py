class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=[]
        star=[]
        for i in range(len(s)):
            if(s[i]=="("):
                left.append(i)
            elif(s[i]=="*"):
                star.append("*")
            else:
                if(left):
                    left.pop()
                elif(star):
                    star.pop()
                else:
                    return False 
        while(left and star):
            l=left.pop()
            s=star.pop()
            if(s<l):
                return False
        return not left 
            
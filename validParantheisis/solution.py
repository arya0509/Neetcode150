
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
                      
            if stack:
                if((stack[-1]=="(" and i==")") or (stack[-1]=="{" and i=="}") or (stack[-1]=="[" and i=="]")):
                    stack.pop()
                    continue

            stack.append(i)
        return len(stack)==0 
    
sol=Solution()
print(sol.isValid("()"))
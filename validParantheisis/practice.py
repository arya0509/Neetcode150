class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s :
            return False
        stack=[]
        for bracket in s:
            if(stack):
                if(bracket==")" and stack[-1]=="(") or (bracket=="}" and stack[-1]=="{") or bracket=="]" and stack[-1]=="[":
                    stack.pop()
                    continue
            stack.append(bracket)
        return len(stack)==0
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for i in tokens:
            if i=='+':
                res= int(stack.pop()) + int(stack.pop())
                stack.append(res)
            elif (i=="-"):
                secondEl=int(stack.pop())
                firstEl=int(stack.pop())
                res= firstEl-secondEl
                stack.append(res)
            elif(i=="*"):
                res=int(stack.pop())*int(stack.pop())
                stack.append(res)
                
            elif(i=='/'):
                secondEl=int(stack.pop())
                firstEl=int(stack.pop())
                res= int(firstEl/secondEl)
                stack.append(int(res))
            else:
                stack.append(i)
        print(stack)
        return stack.pop()
    
sol=Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
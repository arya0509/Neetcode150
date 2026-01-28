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
                res=int(stack
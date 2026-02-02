
class MinStack(object):
    
    
    def __init__(self):
        self.minStack=[]
        self.stack=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if(len(self.minStack)==0 or self.minStack[-1]>=val):
            self.minStack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if(self.minStack[-1]==self.stack[-1]):
            self.minStack.pop()
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
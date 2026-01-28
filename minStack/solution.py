class MinStack(object):
    
    def __init__(self):
        self.stack=[]
        self.minElem=[]
        self.maxElem=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if(len(self.stack)==0 or val<=self.minElem[-1]):
            self.minElem.append(val)
        
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if(self.stack[-1]==self.minElem[-1]):
            self.minElem.pop()
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
       
        return self.minElem[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
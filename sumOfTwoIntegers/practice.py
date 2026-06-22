class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        carry=0
        res=0
        MAX=0x7fffffff
        MASK=0Xffffffff
        for i in range(32):
            aDig=a>>i & 1
            bDig=b>>i & 1
            sum=aDig^bDig^carry
            carry= (aDig+bDig+carry)>1
            res=res|(sum<<i)
        if(res>MAX):
            res=~(res^MASK)
        return res 

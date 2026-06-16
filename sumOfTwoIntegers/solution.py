class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        res=0
        carry=0
        MASK=0xFFFFFFFF
        MAX=0x7FFFFFFF
        for i in range(32):
            
            aBit=a>>i & 1
            bBit=b>>i & 1
            
            currBit=aBit^bBit^carry
            carry=(aBit +bBit +carry)>=2

            if(currBit):
                res=res|(1<<i)
        if(res>MAX):
            res=~(res^MASK)
        
        return res 
            
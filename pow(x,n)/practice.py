class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        r=n
        n=abs(n)
        if(n==0):
            return 1
        if(n==1):
            return x
        if(n%2==0):
            res= self.myPow(x,n/2) 
            res=res *res
        else: 
            res= self.myPow(x,(n-1)/2) 
            res= res * res *x
        if(r<0):
            return 1/res
        return res 
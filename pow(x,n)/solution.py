class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n or n==1:
            return x
        res=x
        r=n
        if(n<0):
            r=-n
        if(n%2==0):
            res=self.myPow(x,r/2)
            res*=res
        else:
            res=self.myPow(x,(r-1)/2)
            res=res*res*x

        if(n<0):
            return 1/res
        return res 
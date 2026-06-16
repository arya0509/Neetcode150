class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n==1):
            return True 
        def returnSquare(num):
            sum=0
            while(num>9):
                last=num%10
                sum+=last*last
                num=num//10
            sum+=num*num
            return sum
        a=returnSquare(returnSquare(n))
        b=returnSquare(n)
        while(a!=b):
            a=returnSquare(returnSquare(n))
            b=returnSquare(n)
            if(a==1):
                return True 
        return False 
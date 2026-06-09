class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.calculated=set()

        def recursion(num):
            sum=0
            while(num):
                val=num%10
                sum+=val*val
                num=num//10
            if(sum==1):
                return True 
            if(sum in self.calculated):
                return False
            self.calculated.add(sum)
            return recursion(sum)
        return recursion(n)

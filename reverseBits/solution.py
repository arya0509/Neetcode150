class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        for i in range(32):
            if(n & (1<<i)):
                res=res|1<<(31-i)
        return res 

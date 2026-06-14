class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        for i in range(32):
            mask=1<<i
            if(mask & n):
                res+=1
        return res 
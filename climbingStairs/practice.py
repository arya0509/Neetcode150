class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one=two=1
        for i in range(2,n+1):
            temp=one
            one+=two
            two=temp
        return one 
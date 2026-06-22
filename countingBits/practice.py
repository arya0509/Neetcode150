class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[0]
        diff=1
        for i in range(n+1):
            if(i==diff*2):
                diff=i
            res.append(1+[res[i-diff]])
        return res 
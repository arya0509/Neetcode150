class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if not n:
            return [0]
        
        res=[0,1]
        prev=2
        for i in range(2,n+1):
            if(prev*2==i):
                prev*=2
            res.append(res[i-prev]+1)       
        return res

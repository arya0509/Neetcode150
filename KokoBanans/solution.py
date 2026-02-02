import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l=1
        r=max(piles)
        res=max(piles)
        while(l<=r):
            mid=r+l//2
            bansPerHour=0
            for p in piles:
                bansPerHour+=math.ceil(p/mid)
            if(bansPerHour<=h):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
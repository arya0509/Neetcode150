import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        piles.sort()

        left=1
        right=k=piles[-1]
        
        while(left<right):
            mid=(right+left)//2

            totalTime=0
            for pile in piles:
                totalTime+= math.ceil(pile/mid)
                if(totalTime>h):
                    break
           
            if(totalTime<=h):
                right=mid-1
                k=min(k,mid)
               
            else:
                left=mid+1
        return k
    
sol=Solution()
print(sol.minEatingSpeed([30,11,23,4,20],5))
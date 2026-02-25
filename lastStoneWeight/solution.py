class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()

        while(len(stones)>1):
            last=stones[-1]
            secondLast=stones[-2]

            stones.pop()
            stones.pop()

            if(last-secondLast>0):
                stones.append(last-secondLast)
                stones.sort()
        
        return stones[0] if(len(stones)==1) else 0
import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i]=-1*stones[i]
        
        heapq.heapify(stones)
        while(len(stones)>1):
            last=heapq.heappop(stones)
            secondLast=heapq.heappop(stones)   

            if(abs(last)-abs(secondLast)>0):
                heapq.heappush(stones,(abs(last)-abs(secondLast))*-1)   

        stones.append(0)

        return stones[0] *-1 
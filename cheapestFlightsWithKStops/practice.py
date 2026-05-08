from collections import deque
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        adj ={i:[] for i in range(n)}
        minCost=[float("inf")]*n
        for flight in flights:
            adj[flight[0]].append((flight[2],flight[1]))
        q=deque()
        q.append(((0,0,src)))
        while(q):
            stops,cost,airp=q.popleft()
            for dsts in adj[airp]:
                if(stops+1>k and dsts[1]!=dst):
                    continue
                if(cost+dsts[0]>minCost[dsts[1]]):
                    continue
                minCost[dsts[1]]=cost+dsts[0]
                q.append(stops+1,cost+dsts[0],dsts[1])
        return minCost[dst] if (minCost[dst]!=float("inf")) else -1
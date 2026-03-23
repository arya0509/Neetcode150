from collections import defaultdict,deque
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
        adj=defaultdict(list)
        for flight in flights:
            adj[flight[0]].append((flight[1],flight[2]))
        q=deque()
        prices=[float("inf")]*n
        prices[src]=0
        q.append((0,src,0))

        while q:
            cst,airp,stops=q.popleft()
            if(stops>k):
                continue
            for nei,p in adj[airp]:
                if(cst+p<prices[nei]):
                    q.append((cst+p,nei,stops+1))

        return prices[dst] if prices[dst]!=float("inf") else -1 
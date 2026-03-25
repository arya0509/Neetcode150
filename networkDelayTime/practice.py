from collections import defaultdict
import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj=defaultdict(list)
        for time in times:
            adj[time[0]].append((time[1],time[2]))
        heap=[(0,k)]
        time=0
        visited=set()
        while heap:
            t,node=heapq.heappop(heap)
            if(node in visited):
                continue
            visited.add(node)
            time=t
            for t1,n1 in adj[node]:
                heapq.heappush(heap,(t1+time,n1))
        
        return time if(len(visited)==n) else -1

            

        
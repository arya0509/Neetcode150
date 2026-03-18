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
        visited=set()
        dictionary=defaultdict(list)
        for time in times:
            dictionary[time[0]].append((time[2],time[1]))
        heap=[(0,k)]
        t=0
        while heap:
            d,n=heapq.heappop(heap)
            if(n in visited):
                continue
            t=max(t,d)
            visited.append(n)
            for d2,n2 in dictionary[n]:
                if(n2 not in visited):
                    heapq.heappush(heap,(d2+d,n2))
        return t if len(visited)==n else -1

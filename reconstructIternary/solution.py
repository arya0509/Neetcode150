from collections import defaultdict
import heapq
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj=defaultdict(list)
        tickets.sort()
        for ticket in tickets:
            heapq.heappush(adj[ticket[0]],ticket[1])
        res=["JFK"]
        def dfs(airport):
            if(len(res)==len(tickets)+1):
                return True
            if(src not in adj):
                return False
            # while(adj[airport]):
            temp=adj[airport][:]
            index=0
            for i in temp:
                src=adj[airport].pop(i)
                res.append(src)
                if(dfs(src)):
                    return True
                adj[airport].insert(index,i)
                res.pop()
            return False
        dfs("JFK")
        return res
                

        
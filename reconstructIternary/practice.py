from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj=defaultdict(list)
        for ticket in tickets.sort()[::-1]:
            adj[ticket[0]].append(ticket[1])
        res=["JFK"]
        def dfs(src):
           while(adj[src]):
               dst=adj[src].pop()
               dfs(dst)
           res.append(src)
        dfs("JFK")
        return res
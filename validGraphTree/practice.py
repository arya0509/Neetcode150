from collections import defaultdict
class Solution:
    def validTree(self, n, edges):
        adj=defaultdict(list)
        unique=set()
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            unique.add(edge[0])
            unique.add(edge[1])
        uniqueTraversal=set()
        visited=set()
        def dfs(e,p):
            uniqueTraversal.add(e)
            if(e in visited):
                return False
            if(e not in adj):
                return True
            visited.add(e)
            for n in adj[e]:
                if(n==p):
                    continue
                if(not dfs(n,e)):
                    return False
            visited.remove(e)
            return True
        
        if(not dfs(0,-1) or len(unique)!=len(uniqueTraversal)):
            return False
        
        return True
        
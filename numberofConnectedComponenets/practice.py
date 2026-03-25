from collections import defaultdict
class Solution:
    def countComponents(self, n, edges):
        adj=defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited=set()
        currPath=set()

        def isUniqueComp(e):
            if(e in visited):
                print(e)
                return False
            visited.add(e)
            currPath.add(e)
            for e1 in adj[e]:
                if(e1 in currPath):
                    continue
                if(not isUniqueComp(e1)):
                    return False
            currPath.remove(e)
            return True 
        res=0
        for i in range(n):
            if(isUniqueComp(i)):
                res+=1
        return res
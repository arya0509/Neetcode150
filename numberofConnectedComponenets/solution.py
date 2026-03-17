from collections import defaultdict
class Solution:
    def countComponents(self, n, edges):
        self.count=0
        nodeDict=defaultdict(list)
        visited=set()
        
        for edge in edges:
            nodeDict[edge[0]].append(edge[1])
            nodeDict[edge[1]].append(edge[0])
        def isDifferentComponent(node,path):
            if(node in path):
                return True
            if(node in visited):
                return False
            visited.add(node)
            path.add(node)
            for n in nodeDict[node]:
                if(not isDifferentComponent(n,path)):
                    path.remove(node)
                    return False
           
            return True
        for node in range(n):
            path=set()
            if(isDifferentComponent(node,path)):
                self.count+=1
        return self.count
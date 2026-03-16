from collections import defaultdict
class Solution(object):
    def validTree(self, n, edges):
        valid=set()
        path=set()
        nodes=defaultdict(list)

        for node in edges:
            nodes[node[0]].append(node[1])
            nodes[node[1]].append(node[0])
        
        def dfs(node,prev):
            if(node in path):
                return False
            path.add(node)
            for n in nodes[node]:
                if(n==prev):
                    continue
                if(not dfs(n,node)):
                    return False
            valid.add(node)
            return True 
        if(not dfs(0,-1)):
            return False
        if(len(valid)!=n):
            print(valid)
            return False
        return True
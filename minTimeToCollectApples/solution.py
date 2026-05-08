class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        
        adj={i:[] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        def dfs(node,par):
           time=0
           for child in adj[node]:
               if(child==par):
                   continue
               childTime=dfs(child,node)
               if(childTime or hasApple[child]):
                   time+childTime+2
            
           return time 
        return dfs(0,-1)
                

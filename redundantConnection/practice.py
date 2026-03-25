class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n=len(edges)
        par=[i for i in range(n)]
        size=[1]*n

        def getParent(e):
            while(e!=par[e]):
                e=par[e]
            return e 
        def connect(e1,e2):
            p1=getParent(e1)
            p2=getParent(e2)
            if(p1==p2):
                return False 
            if(size[p1]>size[p2]):
                par[p2]=p1
                size[p1]+=size[p2]
            else:
                par[p1]=p2
                size[p2]+=p1
            return True 
        for edge in edges:
            if(not (connect(edge[0],edge[1]))):
                return edge
        
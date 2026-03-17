class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n=len(edges)
        parent=[i for i in range(n+1)]
        size=[1]*(n+1)

        def findParent(n):
            if(n==parent[n]):
                return parent[n]
            return findParent(parent[n])
        def union(n1,n2):
            p1=findParent(n1)
            p2=findParent(n2)
            if(n1==3 and n2==5):
                print(p1)
                print(p2)
            if(p1==p2):
                return False
            if (size[p1]>size[p2]):
                parent[p2]=p1
                size[p1]+=size[p2]
            else:
                parent[p1]=p2
                size[p2]+=size[p1]
            return True
        for n1,n2 in edges:
            if(not union(n1,n2)):
                return [n1,n2]
        return [ ]
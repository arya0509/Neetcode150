from collections import defaultdict
import math
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        weights=defaultdict(list)
        edges=[]
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                distance=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                edges.append((distance,j,i))
        edges.sort()
        parent={ tuple(point):point for point in points}
        size={ tuple(point):1 for point in points}

        def getParent(p):
            while((p)!=parent[tuple(p)]):
                p=parent[tuple(p)]
            return p
        def dsu(p1,p2):
            par1=getParent(p1)
            par2=getParent(p2)
            if(par1==par2):
                return False
            if(size[tuple(par1)]>size[tuple(par2)]):
                parent[tuple(par2)]=par1
                size[tuple(par1)]+=size[tuple(par2)]
            else:
                parent[tuple(par1)]=par1
                size[tuple(par2)]+=size[tuple(par1)]
            return True
        count=0
        dist=0
        for edge in edges:
            if(count+1==len(points)):
                break
            if(dsu(points[edge[1]],points[edge[2]])):
                dist+=edge[0]
                count+=1

        return self.distance 

        
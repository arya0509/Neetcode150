import heapq
import math
from collections import defaultdict
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distances=[]
        pointHash=defaultdict(list)
        if not points:
            return 
        for point in points:
            distance=math.sqrt(math.pow(point[0],2)+math.pow(point[1],2))
            distances.append(distance)
            pointHash[distance].append(point)
        
        heapq.heapify(distances)

        res=[]
        while(len(res)<k):
            point=heapq.heappop(distances)
            pointList=pointHash[point]
            if(len(pointHash[distances[0]])>1):
               
               
                while(pointList):
                    if(len(res)==k):
                        break
                    res.append(pointList.pop())
            else:
                res.append(pointList.pop())

        
        return res

        

        
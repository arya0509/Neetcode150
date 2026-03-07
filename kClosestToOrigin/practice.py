import math,heapq
from collections import defaultdict
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap=[]
        hash=defaultdict(list)
        for point in points:
            distance=math.sqrt(math.pow(point[0],2)+math.pow(point[1],2))
            heap.append([-distance,point])
          
        heapq.heapify(heap)
        while(len(heap)>k):
            heapq.heappop(heap)
        res=[]
        for key in heap:
           
            res.append(key[1])
        return res
            
        
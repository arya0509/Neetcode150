import heapq
class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort()
        heap=[]
        size={}
        res=[]
        i=j=0
        while(j<len(queries)):
            while(i<len(intervals) and intervals[i][0]<=queries[j]):
                heapq.heappush(heap,(intervals[i][1]-intervals[i][0]+1,intervals[i][1]))
                i+=1
            while(heap and heap[0][1]<queries[j]):
                heapq.heappop(heap)
            if not heap:
                size[j]=-1
            else:
                size[j]=heap[0][0]
            j+=1
        for i in range(len(queries)):
            res.append(size[i])
         
        return res 
                
        
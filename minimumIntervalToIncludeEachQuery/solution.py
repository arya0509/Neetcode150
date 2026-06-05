import heapq
class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort()
        q=queries[:].sort()
        heap=[]
        order={}
        i=0
        j=0
        res=[]
        while(j<len(queries)):
           
            while(i<len(intervals) and intervals[i][0]<=q[j]):
                start=intervals[i][0]
                end=intervals[i][1]
                heapq.heappush(heap,[end-start+1,end])
                i+=1
            while(heap and heap[0][1]<q[j]):
                heapq.heappop(heap)
            if(not heap):
                order[q[j]]=-1
            else:
                 order[q[j]]= heap[0][0]
            j+=1
        for i in range(len(queries)):
            res.append(order[queries[i]])
        return res 
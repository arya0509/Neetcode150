import heapq
from collections import Counter,deque
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        frequency=Counter(tasks)
        heap=[]
        for key in frequency:
            heapq.heappush(heap,-frequency[key])
           
        q=deque()
        time=0
        while(q or heap):
            time+=1
            if(not heap):
                time=q[0][1]
            else:
                freq=heapq.heappop(heap)
                time+=1
                if(freq+1<0):
                    q.append([freq+1,time+n])
            if(q and time==q[0][1]):
                freq=q.popleft()[0]
                heapq.heappush(heap,freq)
        return time
            


            
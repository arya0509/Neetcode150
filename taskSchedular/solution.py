from collections import Counter,deque
import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count=Counter(tasks)
        maxHeap=[]
        for val in count.values():
            maxHeap.append(-1*val)
        heapq.heapify(maxHeap)
        queue=deque() #[-cnt,time]
        time=0
        while(maxHeap or queue):
            time+=1
            if not maxHeap:
                time=queue[0][1]
            else:
                freq=1+heapq.heappop(maxHeap)
                if freq:
                    queue.append([freq,time+n])
            if(queue and time==queue[0][1]):
                freq=queue.popleft()[0]
                heapq.heappush(maxHeap,freq)
        return time

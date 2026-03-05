import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap=[]
        for stone in stones:
            heap.append(-stone)
        heapq.heapify(heap)
        while(len(heap)>1):
            first=-heapq.heappop(heap)
            second=-heapq.heappop(heap)
            if first-second!=0:
                heapq.heappush(heap,-(first-second))
        heap.append(0)
        return heap[0]
        
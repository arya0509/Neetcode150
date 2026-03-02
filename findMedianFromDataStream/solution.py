import heapq
class MedianFinder(object):

    def __init__(self):
        self.leftHeap=[]
        self.rightHeap=[]
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.leftHeap,-num)
        heapq.heappush(self.rightHeap,-heapq.heappop(self.leftHeap))

        if(len(self.leftHeap)<len(self.rightHeap)):
            heapq.heappush(self.leftHeap,-heapq.heappop(self.rightHeap))
       
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        if((len(self.leftHeap)+len(self.rightHeap))%2==0):
            left=-self.leftHeap[0]
            right=self.rightHeap[0]
            return float(left+right)/2
        else:
            
            val=-self.leftHeap[0]
            return val

           


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
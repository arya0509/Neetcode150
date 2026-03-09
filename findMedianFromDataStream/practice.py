import heapq
class MedianFinder(object):

    def __init__(self):
        self.left=[]
        self.right=[]        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.left,-num)
        heapq.heappush(self.right,-heapq.heappop(self.left))
        
        if len(self.left)<len(self.right):
             heapq.heappush(self.left,-heapq.heappop(self.right))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if(len(self.left)-len(self.right)==1):
            return -self.left[0]
        
        left=-self.left[0]
        right=self.right[0]

        return float(left+right)/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
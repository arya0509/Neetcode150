import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        negativeArray=[]
        for num in nums:
            negativeArray.append(-1*num)
        heapq.heapify(negativeArray)
        val=None
        for i in range(k):
            val=heapq.heappop(negativeArray)
        
        return val * -1
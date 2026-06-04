class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        prevEnd=intervals[0][1]
        res=0
        for i in range(1,len(intervals)):
            interval=intervals[i]
            if(prevEnd>interval[0]):
                res+=1
                prevEnd=min(prevEnd,interval[1])
            else:
                prevEnd=interval[1]
        return res 
                
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        prev=intervals[0][1]
        res=0
        for i in range(1,len(intervals)):
            interval=intervals[i]
            if(prev>interval[0]):
                res+=1

                prev=min(prev,interval[1])
            else:
                prev=interval[1]
        return res 
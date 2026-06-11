class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        overlapping=intervals[0]
        res=[]
        for i in range(1,len(intervals)):
            interval=intervals[i]
            if(overlapping[1]<interval[0]):
                res.append(overlapping)
                overlapping=interval
            else:
                overlapping=[min(overlapping[0],interval[0]),max(overlapping[1],interval[1])]
        if(res[-1]!=overlapping):
            res.append(overlapping)
        return res 

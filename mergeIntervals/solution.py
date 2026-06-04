class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        curr=intervals[0]
        res=[]
        intervals.sort()
        for interval in intervals:
            if(curr[1]>=interval[0]):
                curr=[min(curr[0],interval[0]),max(curr[1],interval[1])]
            else:
                res.append(curr)
                curr=interval
        return res 

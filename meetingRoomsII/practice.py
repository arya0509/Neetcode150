"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals):
        startArr=[]
        endArr=[]
        for interval in intervals:
            startArr.append(interval.start)
            endArr.append(interval.end)
        startArr.sort()
        endArr.sort()

        start=0
        end=0
        res=0
        r=0
        while(start<len(startArr) and end<len(endArr)):
            if(startArr[start]<endArr[end]):
                r+=1
                res=max(res,r)
                start+=1
            else:
                r-=1
                end+=1
        return res 

        
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return True 
        
        start=[]
        end=[]
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        currMax=0
        curr=0
        s=e=0
        while(s<len(start) and e<len(end)):
            if(start[s]<end[e]):
                s+=1
                curr+=1
            else:
                e+=1
                curr-=1
            currMax=max(curr,currMax)
        return currMax





       

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, interval):
        if not interval:
            return True 
        interval.sort(key=lambda x:x.start)

        prev=interval[0][1]
        for i in range(1,len(interval)):
            curr=interval[i]
            if(prev>curr[0]):
                return False
            prev=curr[1]
        return True 

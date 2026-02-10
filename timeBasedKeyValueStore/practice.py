from collections import defaultdict
class TimeMap(object):

    def __init__(self):
        self.keyTimeValDict=defaultdict(list)
    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.keyTimeValDict[key].append([timestamp,value])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        timeValList=self.keyTimeValDict[key]
        l=0
        r=len(timeValList)-1
        res=""
        while(l<=r):
            mid=(l+r)//2
            if(timeValList[mid][0]<=timestamp):
                res=timeValList[mid][0]
                l=mid+1

            else:
                r=mid-1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
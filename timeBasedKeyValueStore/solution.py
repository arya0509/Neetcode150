from collections import defaultdict
class TimeMap(object):
    
    def __init__(self):
        self.KeyTimeDict= defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        
        self.KeyTimeDict[key].append([timestamp,value])
        print(self.KeyTimeDict[key])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        listOfKey=self.KeyTimeDict.get(key,"")
       
        if(listOfKey==""):
            return ""
        l=0
        r=len(listOfKey)-1
        while(l<=r):
            mid=r+l//2
            if(listOfKey[mid][0]<=timestamp):
                l=mid+1
                while(mid+1!=len(listOfKey) and listOfKey[mid+1][0]<=timestamp):
                    mid+=1
                return listOfKey[mid][1]

            if(listOfKey[mid][0]>timestamp):
                r=mid-1
            

        return ""
        


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
param_2 = obj.get("foo",1)
print(param_2)
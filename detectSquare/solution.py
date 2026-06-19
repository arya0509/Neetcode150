class DetectSquares(object):

    def __init__(self):
        self.freq={}

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.freq[tuple(point)]=self.freq.get(tuple(point),0)+1
        

    def count(self, point):
        """a
        :type point: List[int]
        :rtype: inta
        """
        x1=point[0]
        y1=point[1]
        res=0
        for point in self.freq:
            x2=point[0]
            y2=point[1]
            if (x1-x2==y1-y2) and x1!=x2:
                if((x1,y2) in self.freq and (x2,y1) in self.freq):
                    p1=self.freq[point]
                    p2=self.freq[(x1,y2)]
                    p3=self.freq[(x2,y1)]
                    p4=self.freq.get((x2,y2),1)
                    res+=p1*p2*p3*p4
        return res 
                    
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
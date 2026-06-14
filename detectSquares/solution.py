class DetectSquares(object):

    def __init__(self):
        self.points=set()
        self.c={}
        

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.points.add((point[0],point[1]))
        self.c[(point[0],point[1])]=self.c.get((point[0],point[1]),0)+1

        

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        res=0
        for p in self.points:
           
           if(abs(point[0]-p[0])==abs(point[1]-p[1]) and p!=(point[0],point[1])):
                point1=(point[0],p[1])
                point2=(p[0],point[1])
                print(point1)
                print(point2)
                if(point1 in self.points and point2 in self.points):
                    res+=self.c[point1]*self.c[point2]
        return res 
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
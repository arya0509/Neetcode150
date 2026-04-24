class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        point_dict={}
        length={}
        distance=[]
        res=0
        
        for point in points:
            point_dict[tuple(point)]=point
            length[tuple(point)]=1
            for others in points:
                if(others==point):
                    continue
                val=abs(point[0]-others[0])+abs(point[1]-others[1])
                distance.append((val,point,others))
        distance.sort()
        def getParent(point):
            if(point_dict(tuple(point))==point):
                return point
            return getParent(point_dict(tuple(point)))
        count=1
        for val in distance:
            if(count+1==len(points)):
                break
            p1=getParent(val[1])
            p2=getParent(val[2])
            if(p1==p2):
                continue
            if(length[tuple(p1)]>length[tuple(p2)]):
                point_dict[tuple(p2)]=p1
                length[tuple(p1)]+=length[tuple(p2)]
            else:
                
                point_dict[tuple(p1)]=p2
                length[tuple(p2)]+=length[tuple(p1)]
            
            res+=val[0]
            count+=1
        return res


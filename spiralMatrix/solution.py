class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left=0
        right=len(matrix[0])-1
        up=0
        bottom=len(matrix)-1
        res=[]
        while(left<right and up<bottom):
           
            for i in range(left,right+1):
                res.append(matrix[up][i])
            up+=1
            for i in range(up,bottom+1):
                res.append(matrix[i][right])
            right-=1
            #a check here

            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            
            bottom-=1
            for i in range(bottom,up-1,-1):
                res.append(matrix[i][left])
            left+=1
            print(left)
            print(right)
        return res 
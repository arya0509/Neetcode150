class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
           
            if(row[-1]>=target):
                half=len(row)//2
                
                if(row[half]>=target):
                    for col in range(half+1):
                        if row[col]==target:
                            return True
                        
                else:
                    for col in range(half+1,len(row)):
                        if row[col]==target:
                            return True
        return False
    
sol=Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3),)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if[row[-1]>=target]:
                left=0
                right=len(row)-1
                while(left<=right):
                    mid=(left+right)//2

                    if(target==row[mid]):
                        return True
                    elif(target>row[mid]):
                        left=mid+1
                    else:
                        right=mid-1
        return False
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        max_area=0
        smallest=0
        
        while(left<right ):
            if(height[left]>height[right]):
                
                smallest=right
            else:
                
                smallest=left

            
            area=height[smallest] * (right-left)
            
            if(area>max_area):
                
                max_area=area

            if(height[left]>=height[right]):
                right-=1
            else:
                left+=1
            

        return max_area

sol=Solution()
print(sol.maxArea([1,2,4,3]))
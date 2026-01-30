class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxLeft=height[0]
        maxRight=height[-1]
        water=0
        l=0
        r=len(height)-1
        while(l!=r):
            if(height[l]<height[r]):
                l+=1
                maxLeft=max(maxLeft,height[l])
                water+=maxLeft-height[l]

            else:
                r-=1
                maxRight=max(maxRight,height[r])
                water+=maxRight-height[r]
        
        return water

sol=Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
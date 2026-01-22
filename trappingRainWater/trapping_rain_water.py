class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        l=0
        r=len(height)-1

        res=0
        maxLeft=height[l]
        maxRight=height[r]
        
        while(l<r):
            if(maxLeft<maxRight):
                l+=1
                maxLeft=max(maxLeft,height[l])
                res+=maxLeft-height[l]
            
            else:
                r-=1
                maxRight=max(maxRight,height[r])
                res+=maxRight-height[r]


        return res
sol=Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

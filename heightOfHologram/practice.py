class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        smallLeft=[-1]*len(heights)
        for height in range(len(heights)):
            while(stack and heights[stack[-1]]>=heights[height]):
                stack.pop()
            
            if(stack):
                smallLeft[height]=(stack[-1])
            stack.append(height)
            
        
        stack=[]
        smallRight=[len(heights)] *len(heights)

        for height in range(len(heights)-1,-1,-1):
            while(stack and heights[stack[-1]]>=heights[height]):
                stack.pop()
            
            if(stack):
                smallRight[height]=(stack[-1])
            stack.append(height)    
        
        maxArea=0

        for height in range(len(heights)):
            left=smallLeft[height]+1
            right=smallRight[height]-1
            area=heights[height] * (right-left+1)
            maxArea=max(maxArea,area)
        
        return maxArea

sol=Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        n=len(heights)
        leftMost=[-1] * n
        for i in range(n):
            while(stack and heights[i]<=heights[stack[-1]]):
                stack.pop()
            if(stack):
                leftMost[i]=stack[-1]
            stack.append(i)
       
        stack=[]
        rightMost=[n] * n
        for i in range(n-1,-1,-1):
            while(stack and heights[i]<=heights[stack[-1]]):
                stack.pop()         
            if(stack):
                rightMost[i]=stack[-1]
            stack.append(i)

        maxArea=0
        for i in range (n):
            leftMost[i]+=1
            rightMost[i]-=1
            area=heights[i] *((rightMost[i]-leftMost[i])+1)
            maxArea=max(area,maxArea)
        return maxArea
    
sol=Solution()
print(sol.largestRectangleArea([2,4]))
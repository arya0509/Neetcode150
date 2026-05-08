class Solution:
    def findBuildings(self, heights):
        maxIndx=len(heights)-1
        res=[heights[maxIndx]]
        for i in range(maxIndx,-1,-1):
            if(heights[i]>heights[maxIndx]):
                maxIndx=i
                res.append(i)
        return res[::-1]
        
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        indexStack=[]
        res=[0]*len(temperatures)

        for index in range(len(temperatures)):
            while(indexStack and temperatures[index]>temperatures[indexStack[-1]]):
                indx=indexStack.pop()
                res[indx]=index-indx+1
            indexStack.append(index)
        while(len(indexStack)!=0):
            indx=indexStack.pop()
            res[indx]=0
        
        return res




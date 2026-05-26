class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        startIndex=0
        currFuel=0
        for i in range(len(gas)):
            currFuel+=gas[i]-cost[i]
            if(currFuel<0):
                startIndex=i+1
                currFuel=0
        return startIndex if currFuel>=0 else -1 
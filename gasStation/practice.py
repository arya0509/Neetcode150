class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum=0
        total=0
        start=0
        for i in range(len(gas)):
            cst=gas[i]-cost[i]
            sum+=cst 
            total+=cst
            if(sum<0):
                start=i+1
                sum=0
            
        return -1 if total<0 else start
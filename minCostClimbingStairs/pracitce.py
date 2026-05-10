class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        one=cost[1]
        two=cost[0]
        n=len(cost)
        for i in range(2,n):
            temp=one
            one=cost[i]+min(one,two)
            two=temp
        return min(one,two)

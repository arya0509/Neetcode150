class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        one =cost[-2]
        two=cost[-3]
        for i in range(len(cost)-2,-1,-1):
            temp=cost[i]+min(one,two)
            two=one
            one=temp
        return min(one,two)
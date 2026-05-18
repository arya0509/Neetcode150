class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cache={}
        def dfs(sum,i):
            if(sum==target and i==len(nums)):
                return 1
            if(i==len(nums)):
                return 0
            if((sum,i) not in cache):
                res= dfs(sum+nums[i],i+1) + dfs(sum-nums[i],i+1)
                cache[(sum,i)]=res
            return cache[(sum,i)]
        return dfs(0,0)
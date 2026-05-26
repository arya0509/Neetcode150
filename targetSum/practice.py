class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo={}
        def dfs(sum,i):
            if(i==len(nums)):
                if(sum==target):
                    return 1
                return 0
            
            if (sum,i) in memo:
                return memo[(sum,i)]
            res1=dfs(sum+nums[i],i+1)
            res2=dfs(sum-nums[i],i+1)
            memo[(sum,i)]= res1+res2
            if(i==0):
                print(res1)
                print(res2) 
            return memo[(sum,i)]
        res=dfs(0,0)
       
        return res
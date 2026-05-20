class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum=0
        for num in nums:
            sum+=num
        if(sum%2!=0):
            return False
        memo={}
        def dfs(sum,i):
            if(sum==0):
                return True 
            if(i==len(nums) or sum<0):
                return False
            if((sum,i) in memo):
                return memo[(sum,i)]
            memo[(sum,i)]=dfs(sum-nums[i],i+1) or dfs(sum,i+1)
            return memo[(sum,i)]
        return dfs(sum%2,0)
            
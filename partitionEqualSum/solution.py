class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.cache={}
        self.sum=0
        for num in nums:
            self.sum+=num
        if(self.sum%2!=0):
            return False
        self.target=self.sum/2
        def dfs(sum,i):
            if(sum==self.target):
                return True 
            if(sum>self.target):
                return False 
            if(i==len(nums)):
                return False 
            if((sum,i) not in self.cache):
                ans=dfs(sum+nums[i],i+1) or dfs(sum,i+1)
                self.cache[(sum,i)]=ans
            return self.cache[(sum,i)] 
            
            
        return dfs(0,0)
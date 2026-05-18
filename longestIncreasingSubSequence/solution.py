class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.cache={}
        def dfs(prev,indx):
            if(indx==len(nums)):
                return 0
            maxAns=0
            for i in range(indx,len(nums)):
                if(nums[i]>prev):
                    if(i not in self.cache):
                        ans=dfs(nums[i],i+1)
                        self.cache[i]=ans+1
                    maxAns=max(self.cache[i],maxAns)
            return maxAns
            
        maxLen=0
        for i in range(len(nums)):
            if(i not in self.cache):
                dfs(nums[i]-1,i)
            maxLen=max(maxLen,self.cache[i])
        print(self.cache[0])
        return maxLen            
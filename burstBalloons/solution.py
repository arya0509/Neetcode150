class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[1]+nums+[1]
        memo={}
        def dfs(l,r):
            if(l>r):
                return 0
            if((l,r) in memo):
                return memo[(l,r)]
            memo[(l,r)]=0
            for i in range(l,r+1):
                coins=nums[i-1]*nums[i]*nums[i+1]
                coins+=dfs(l,i-1)+dfs(i+1,r)
                memo[(l,r)]=max(coins,memo[l,r])
            return memo[(l,r)]
       
        return dfs(1,len(nums)-2)
            
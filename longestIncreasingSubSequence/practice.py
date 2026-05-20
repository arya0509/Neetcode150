class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo={}
        def dfs(i,prev):
            if(i==len(nums)):
                return 0
            maxVal=0
            for idx in range(i,len(nums)):
                if(nums[idx]>prev):
                    if(idx not in memo):
                        res=1+dfs(idx+1,nums[idx])
                        memo[idx]=res
                    maxVal=max(memo[idx],maxVal)
            return maxVal
        # maxVal=0
        # for num in range(len(nums)):
        #     res=dfs(num,float("-inf"))
        #     maxVal=max(res,maxVal)
        return dfs(0,float("-inf"))

        


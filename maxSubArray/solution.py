class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        maxSum=nums[0]

        currSum=nums[0]

        for i in range(1,len(nums)):
            if(nums[i]>currSum+nums[i]):
                currSum=nums[i]
            else:
                currSum+=nums[i]
            maxSum=max(maxSum,currSum)
        return maxSum
        


        
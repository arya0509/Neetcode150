class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix=[0] * len(nums)
        suffix=[0] * len(nums)

        prefix[0]=1
        suffix[len(nums)-1]=1
        output=[0] * len(nums)

        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            suffix[i]=suffix[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            output[i]=suffix[i] * prefix[i]

        return output
            

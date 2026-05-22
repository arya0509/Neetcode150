class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        sum=nums[0]
        res=sum
        for num in nums:
            sum=max(sum+num,num)
            res=max(sum,res)
        return res 
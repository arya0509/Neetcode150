class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        sum=float("-inf")
        res=sum
        for num in nums:
            sum=max(sum+num,num)
            res=max(sum,res)
        return res 
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        maxSum=0
        for num in nums:
            if num+s>num:
                s+=num
            else:
                s=num
            maxSum=max(maxSum,s)
        return maxSum
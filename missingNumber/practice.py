class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for num in nums:
            res^=num
        for i in range(len(nums)):
            res^=nums[i]
        return res 
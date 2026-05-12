class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=nums[0]
        currMax=1
        currMin=1
        for num in nums:
            temp=currMax*num
            currMax=max(currMax*num,currMin*num,num)
            currMin=min(temp,currMin*num,num)
            res=max(currMax,res)
            
        return res 
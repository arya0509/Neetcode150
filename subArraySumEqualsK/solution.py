class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res=0
        currSum=0
        prefixSum={0:1}
        for num in nums:
            currSum+=num
            diff= currSum-k
            res+=prefixSum.get(diff,0)
            prefixSum[currSum]=1+prefixSum.get(currSum,0)



          


            
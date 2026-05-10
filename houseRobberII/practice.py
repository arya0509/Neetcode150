class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(self.robMax(nums[:len(nums)-2]),self.robMax(nums[1:len(nums)-1]))
    def robMax(self,nums):
        if(len(nums)<=2):
            return max(nums)
        maxNums=[num for num in nums]
        maxNums[2]+=maxNums[0]
        val=0
        for i in range(3,len(nums)):
            two=nums[i]+maxNums[i-2]
            three=nums[i]+maxNums[i-3]
            maxVal=max(two,three)
            maxNums[i]=maxVal
            val=max(val,maxVal)
        return val
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=r=0
        minLen=len(nums)+1
        currSum=0
        while(r<len(nums)):
            currSum+=nums[r]
            while(currSum>=target):
                if(l>r):
                    break
                minLen=min(minLen,r-l+1)
                currSum-=nums[l]
                l+=1
               
            r+=1
            
        return minLen if(minLen<len(nums)+1) else 0

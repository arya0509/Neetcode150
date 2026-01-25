class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if(len(nums)==1):
            return nums
        if(k>=len(nums)):
            return [max(nums)]
        l=0
        res=[]
        for r in range (k,len(nums)):
            
            res.append(max(nums[l:r]))
            l+=1
            if(r==len(nums)-1):
                res.append(max(nums[l:r+1]))
        return res
sol=Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
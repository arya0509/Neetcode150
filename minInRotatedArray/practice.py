class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        minNum=nums[0]
        while(l<=r):
            mid=(l+r)//2
            minNum=min(minNum,nums[mid])

            if(nums[mid]>nums[r]):
                l=mid+1
            else:
                r=mid-1
        
        return minNum
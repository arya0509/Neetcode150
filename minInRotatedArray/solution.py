class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        
        while(l<=r):
           
            mid=(l+r)//2
            if(mid==l or mid ==r):
                return min(nums[l],nums[r])
            if(nums[mid]<nums[r]):
                 r=mid
            else:
                l=mid
           
sol=Solution()
print(sol.findMin([3,4,5,1,2]))
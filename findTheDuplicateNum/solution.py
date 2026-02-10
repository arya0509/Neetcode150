class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast=0
        slow=0
        while(True):
            slow=nums[slow]
            fast=nums[nums[fast]]
            if(slow==fast):
                break
        
        slow2=0
        while(True):
            slow=nums[slow]
            slow2=nums[slow2]
            if(slow2==slow):
                return slow
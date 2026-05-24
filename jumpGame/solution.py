class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.goal=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if(i+nums[i]>=self.goal):
                self.goal=i
        return self.goal==0
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        half=len(nums)/2
        if(target)<=nums[half]:
            for i in range(half+1):
                if(nums[i]==target):
                    return i
        else:
            for i in range(half+1,len(nums)):
                if(nums[i]==target):
                    return i
        return -1
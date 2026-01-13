class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict=dict()
        for i in range(len(nums)):
            if(nums_dict.get(target-nums[i])!=None):
                return [nums_dict.get(target-nums[i]),i]
            nums_dict[nums[i]]=i
        
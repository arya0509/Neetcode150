class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       
        Dict=dict()

        for i in range(len(nums)):
            if(Dict.get(target-nums[i])!=None):
                return [Dict.get(target-nums[i]),i]
            Dict[nums[i]]=i
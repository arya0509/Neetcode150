class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict={}
        for i in range(len(nums)):
            num=nums[i]
            if(nums_dict.get(target-num)!=None):
                return [i,nums[target-num]]
            nums_dict[num]=i

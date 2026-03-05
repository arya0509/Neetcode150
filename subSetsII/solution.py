class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        subSet=[]
        nums.sort()
        def backTracking(index):
            if(len(subSet)==len(nums)):
                res.append(subSet[:])
                return 
            if(index>=len(nums)):
                return 
            subSet.append(nums[index])
            backTracking(index+1)

            while(index+1<len(nums) and nums[index]==nums[index+1]):
                index+=1
            subSet.pop()
            backTracking(index+1)
        backTracking(0)
        return res
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        combination=[]
        def backtracking(index):
            if(index==len(nums)):
                res.append(combination[:])
                return 
            combination.append(nums[index])
            backtracking(index+1)
            combination.pop()
            while(index+1<len(nums) and nums[index]==nums[index+1]):
                index+=1
            backtracking(index+1)

        backtracking(0)
        return res
            
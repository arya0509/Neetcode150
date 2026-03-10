class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        combination=[]

        def backtracking(index):
            if(index==len(nums)):
                res.append(combination[:])
                return 
            combination.append(nums[index])
            backtracking(index+1)
            combination.pop()
            backtracking(index+1)
        backtracking(0)
        return res
        

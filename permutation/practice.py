class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        permutation=[]
        def backtracking(visited):
            if(len(permutation)==len(nums)):
                res.append(permutation[:])
                return 
            for i in range(len(nums)):
                if(not visited[i]):
                    permutation.append(nums[i])
                    visited[i]=True
                    backtracking(visited)
                    permutation.pop()
                    visited[i]=False
        backtracking([False]*len(nums))
        return res
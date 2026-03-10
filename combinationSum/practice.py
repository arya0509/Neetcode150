class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        combination=[]
        def backtracking(sum,index):
            if(sum==target):
                res.append(combination[:])
                return 
            elif (sum>target or index==len(candidates)):
                return 
            
            combination.append(candidates[index])
            backtracking(sum+candidates[index],index)
            combination.pop()
            backtracking(sum,index+1)
        backtracking(0,0)
        return res
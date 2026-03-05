class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        combination=[]
        def dfs(i,sum):
            if(sum==target):
                if(combination not in res):
                    res.append(combination[:])
                return 
            elif(sum>target or i>=len(candidates)):
                return 
            combination.append(candidates[i])
            sum+=candidates[i]
            dfs(i,sum)
            
            combination.pop()
            sum-=candidates[i]
            dfs(i+1,sum)
        dfs(0,0)
        return res
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        combination=[]
        def backTracking(index,sum):
            if(sum==target):
                res.append(combination[:])
                return 
            elif(sum>target or index==len(candidates)):
                return 
            combination.append(candidates[index])
            backTracking(index+1,sum+candidates[index])
            while(index+1!=len(candidates) and candidates[index]==candidates[index+1]):
                index+=1
            combination.pop()
            backTracking(index+1,sum)
        backTracking(0,0)
        return res
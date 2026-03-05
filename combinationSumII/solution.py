class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        combination=[]
        sortedCombination={}
        candidates.sort()
        def recursion(sum,index):
            if(sum==target):
                copy=combination[:]
                copy.sort()
                
                res.append(copy)
                   
                    
                return 

            if(sum>target or index>=len(candidates)):
                return    
            if(candidates[index]>target):               
                recursion(sum,index+1)
            else:
                
                combination.append(candidates[index])
                recursion(sum +candidates[index],index+1)

                while(index+1<len(candidates) and candidates[index]==candidates[index+1]):
                    index+=1

               
                combination.pop()
                recursion(sum,index+1)
        recursion(0,0)
        return res

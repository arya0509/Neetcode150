class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.open=0
        self.close=0
        res=[]
       

        def backTracking(combination,open,close):
            if(len(combination)==2*n):
                
                res.append(combination)
                return 
           
            if(open<n):
                backTracking(combination+"(",open+1,close)
            if(close<open):
                backTracking(combination+")",open,close+1)
        backTracking("",0,0)
        return res
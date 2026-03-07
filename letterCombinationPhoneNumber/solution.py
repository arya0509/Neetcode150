class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res=[]
       
        digitDict={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def backtracking(i,string):
            if(i==len(digits)):
                res.append(string)
                return 
            digit=digits[i]
            for char in digitDict[digit]:
                backtracking(i+1,string+char)
        backtracking(0,"")
        return res
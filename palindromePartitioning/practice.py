class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]
        combination=[]
        def isPalindrome(string):
            return string==string[::-1]
        def backtracking(start,string):
            if(start==len(s)):
                res.append(combination[:])
                return 
            for i in range(start,len(s)):
                string+=s[i]
                if(isPalindrome(string)):
                    combination.append(string)
                    backtracking(i+1,"")
                    combination.pop()
        backtracking(0,"")
        return res
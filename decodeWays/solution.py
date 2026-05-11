class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache={len(s):1}
        def backtracking(index):
            if(index in cache):
                return cache[index]
            if(s[index]=="0"):
                return 0
            res=backtracking(index+1)
            if((index+1<len(s)) and ((s[index]=="1") or (s[index]=="2" and s[index+1]<"7" ))):
                cache[index]= res+backtracking(index+2)
                return cache[index]
            cache[index] =res
            return cache[index] 
           
        return backtracking(0)
            
            
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]
        subsets=[]
        def backTracking(index):
            if(index==len(s)):             
                if(not subsets):
                    return
                res.append(subsets[:])            
                return 
            for end in range(index,len(s)):
                string=s[index:end+1]
                if(isPalindrome(string)):
                    subsets.append(string)
                    backTracking(end+1)
                    subsets.pop()
                    
                
            

        def isPalindrome(string):
            start=0
            end=len(string)-1
            while(start<=end):
                if(string[start]!=string[end]):
                    return False
                start+=1
                end-=1
            
            return True
        backTracking("",0)
        return res
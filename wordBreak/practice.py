class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        cache={}
        def dfs(s):
            if not s:
                return True 
            for word in wordDict:
                if word in s:
                    i=s.find(word)
                    left=s[:i]
                    right=s[i+len(word):]
                    if(left not in cache):
                        leftRes=dfs(left)
                        cache[left]=leftRes
                    if(right not in cache):
                        rightRes=dfs(right)
                        cache[right]=rightRes
                    if(cache[left] and cache[right]):
                        return True 

            return False  
        return dfs(s)
            
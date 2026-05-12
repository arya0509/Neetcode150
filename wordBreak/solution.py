class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.cache={}
        def dfs(word):
            if(word==""):
                return True 
            for w in wordDict:
                if(w in word):
                    if(len(w)==len(word)):
                        return True
                    startIndex=word.find(w)
                    if(word[0:startIndex] not in self.cache):
                        left=dfs(word[0:startIndex])
                        self.cache[word[0:startIndex]]=left
                    if(word[startIndex+len(w):] not in self.cache):
                        right=dfs(word[startIndex+len(w):])
                        self.cache[word[startIndex+len(w):]]=right
                    left=self.cache[word[0:startIndex]]
                    right=self.cache[word[startIndex+len(w):]]
                    res=left and right
                    if(res):
                        return True
        res=dfs(s)
        return res if res else False
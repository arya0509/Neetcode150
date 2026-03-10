class TrieNode(object):
    def __init__(self,isEnd=False):
        self.root={}
        self.isEnd=isEnd
class WordDictionary(object):

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr=self.root
        for c in word:
           
            if(c not in curr.root):
                curr.root[c]=TrieNode()
            curr=curr.root[c]
        curr.isEnd=True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr=self.root
        def recursion(curr,word):
            for c in range(len(word)):
                if(word[c] not in curr.root):
                    if(word[c]=="."):
                        for key in curr.root:
                            if(recursion(curr.root[key],word[c+1:])):
                                return True 
                    return False
                curr=curr.root[word[c]]
            return curr.isEnd 
        return recursion(curr,word)



        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
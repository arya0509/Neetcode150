class TrieNode(object):
    def __init__(self,isEnd=False):
        self.children={}
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
            if(c not in curr.children):
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.isEnd=True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
       
        def recursion(word,root):
            curr=root
            for c in range(len(word)):
                if(word[c] not in curr.children):
                    if(word[c]=="."):
                        for key in curr.children:
                            if(recursion(word[c+1:],curr.children[key])):
                                return True
                    return False
                
                curr=curr.children[word[c]]

            return curr.isEnd
        return recursion(word,self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
class TrieNode(object):
    def __init__(self,isEnd=False):
        self.root={}
        self.isEnd=isEnd
class Trie(object):
    

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr=self.root
        for c in word:
            if c not in curr.root:
                curr.root[c]=TrieNode()
            curr=curr.root[c]
        curr.isEnd=True        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr=self.root
        for c in word:
            if(c not in curr.root):
                return False
            curr=curr.root[c]
        return curr.isEnd
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr=self.root
        for c in prefix:
            if(c not in curr.root):
                return False
            curr=curr.root[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
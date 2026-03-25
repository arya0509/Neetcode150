from collections import deque,defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        adj=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                seq=word[:i]+"*"+word[i+1:]
                adj[seq].append(word)
        
        path=set()
        self.minPath=len(wordList)
        q=deque()
        q.append(beginWord)
        res=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if(word in path):
                    continue
                path.add(word)
                if(word==endWord):
                    return res
                for i in range(len(word)):
                    seq=word[:i]+"*"+word[i+1:]
                    if(seq not in adj):
                        continue
                    for w in adj[seq]:
                        if(w not in path):
                            q.append(w)
            res+=1
        return res if(res>1) else 0
                
       

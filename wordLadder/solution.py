from collections import defaultdict,deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dictionary=defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for w in range(len(word)):
                pattern=word[:w]+"*"+word[w+1:]
                dictionary[pattern].append(word)
        res=1
        q=deque([beginWord])
        visited=set([beginWord])
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if(word==endWord):
                    return res
                for w in range(len(word)):
                    pattern=word[:w]+"*"+word[w+1:]
                    for j in dictionary[pattern]:
                        if j not in visited:
                            visited.add(j)
                            q.append(j)
            res+=1
        return 0


        
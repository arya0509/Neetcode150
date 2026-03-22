from collections import defaultdict
class Solution:
    def foreignDictionary(self, words):
        adj={c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            minLen=min(len(w1),len(w2))
            if(len(w1)>len(w2) and w1[:minLen]==w2[:minLen]):
                return ""
            for j in range(minLen):
                if(w1[j]!=w2[j]):
                    adj[w1[j]].add(w2[j])
                    break
        

        visited={}
        res=[]
        def dfs(w):
            if(w in visited):
                return visited[w]
            visited[w]=True
            for w2 in adj[w]:
                if(dfs(w2)):
                    return True
            visited[w]=False
            res.append(w)
            return False 
        for w in adj:
            if(dfs(w)):
                return ""
        return "".join(res[::-1])
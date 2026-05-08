from collections import defaultdict
class Solution:
    def foreignDictionary(self, words):
        adj={c:[]  for w in words for c in w }
        visited={}
        for i in range(len(words)-1):
            first=words[i]
            second=words[i+1]
            minLen=min(len(first),len(second))
            for j in range(min(len(first),len(second))):
                if(len(first)>len(second) and first[:minLen]==second[:minLen]):
                    return ''
                if(first[j]==second[j]):
                    continue
                adj[first[j]].append(second[j])
                break
        res=[]
        def dfs(letter):
            if(letter in visited):
                return visited[letter]
            
            visited[letter]=True
            for word in adj[letter]:
                if(dfs(word)):
                    return True
            res.append(letter)
            visited[letter]=False
            return False
        for word in adj:
            if(dfs(word)):
                return ""
        return "".join(res[::-1]) 
        
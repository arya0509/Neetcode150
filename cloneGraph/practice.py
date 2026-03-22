
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited={}
        def dfs(n):
            if n.val in visited:
                return visited[n.val]
            newNode=Node(n.val)
            visited[n.val]=newNode
            for neighbors in n.neighbors:
                newNode.neighbors.append(dfs(neighbors))
            return newNode
        n=dfs(node)
        return n
            
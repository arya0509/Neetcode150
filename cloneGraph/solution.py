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
        if not node:
            return node
        nodeDict={}
        def recursion(oldNode):
            if(nodeDict.get(oldNode.val,"notFound")!="notFound"):
                return 
            node = Node(oldNode.val)
            nodeDict[node.val]=node
            neighbors=[]
            for neighbor in oldNode.neighbors:
                neighbors.append(recursion(neighbor))
            node.neighbors=neighbors
            return node 
        newNode=recursion(node)
        return newNode
        
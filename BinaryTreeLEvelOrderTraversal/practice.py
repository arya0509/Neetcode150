from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        levelDict=defaultdict(list)

        def addLevel(root,level):
            if not root:
                return None
            
            levelDict[level].append(root.val)
            level+=1
            addLevel(root.left,level)
            addLevel(root.right,level)
        addLevel(root,0)
        res=[]

        for i in range(len(levelDict)):
            res.append(levelDict[i])
        
        return res
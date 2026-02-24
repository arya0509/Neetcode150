# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        levelDict={}

        def levelDown(root,level):
            if not root:
                return 
            if(levelDict.get(level,"None")=="None"):
                levelDict[level]=root.val
            level+=1
            levelDown(root.right,level)
            levelDown(root.left,level)
        
        levelDown(root,0)
        res=[]
        for k in levelDict:
            res.append(levelDict[k])


        return res
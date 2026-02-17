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
        numDict={1:root.val}
        def recursion(root,level):
            val=numDict.get(level,"None")
            if not root:
                return 
            if val=="None":
                recursion(root.right,level+1)
                recursion(root.left,level+1)
            else:
        
                numDict[level]=root.val
                level+=1
                recursion(root.right,level)
                recursion(root.left,level)
            
        recursion(root.right,2)
        recursion(root.left,2)

        res=[]
        for level in range(1,len(numDict)+1):
            res.append(numDict[level])

        return res

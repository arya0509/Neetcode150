# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if(not root):
            return None
        
        left=root.left
        right=root.right

        root.left,root.right=right,left
        self.invertTree(left)
        self.invertTree(right)

        return root
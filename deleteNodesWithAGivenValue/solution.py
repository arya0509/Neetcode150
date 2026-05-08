# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: int
        :rtype: Optional[TreeNode]
        """
        def dfs(value):
            if not value:
                return None
            value.left=dfs(value.left)
            value.right=dfs(value.right)
            if value.val==target and not value.left and not value.right:
                return None
            return value
        if not dfs(root):
            return None
        return root
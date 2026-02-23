# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root :
            return 
        maxPath=[root.val]

        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            maxPath[0]=max(maxPath[0],root.val,root.val + left,root.val+right,root.val+right+left)

            return max(root.val,root.val + left,root.val+right)
        dfs(root)

        return maxPath[0]
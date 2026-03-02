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

        self.maxVal=root.val
        def dfs(root):
            if not root:
                return 0
            leftSum=dfs(root.left)
            rightSum=dfs(root.right)

            self.maxVal=max(self.max,root.val,leftSum+root.val,rightSum+root.val,leftSum+rightSum+root.val)

            return max(leftSum +root.val,rightSum + root.val,root.val)

        dfs(root)
        
        return self.maxVal
        
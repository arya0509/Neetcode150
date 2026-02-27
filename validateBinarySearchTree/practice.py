# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(root,min,max):
            if not root:
                return 
            if(not root.val>min or not root.val<max):
                return False
            validate(root.left,min,root.val)
            validate(root.right,root.val,max)
        validate(root,float("-inf"),float("inf"))
        return True
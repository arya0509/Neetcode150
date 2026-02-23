# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        

        if not root:
            return True
        
        def recursion(root):
            if not root:
                return 0
            
            left=recursion(root.left)
            right=recursion(root.right)

            if (left=="False" or right=="False"):
                return "False"
            
            if(abs(right-left)>1):
                return "False"
            
            return 1+max(left,right)
        val=recursion(root)
        if(val=="False"):
            return False
        return True
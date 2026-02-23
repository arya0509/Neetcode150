# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        maxPath=[0]

        def maxDiameter(root):
            if not root:
                return 0
            
            left=maxDiameter(root.left)
            right=maxDiameter(root.right)

            
            maxPath[0]=max(maxPath[0],left+right)

            return 1+ max(left,right)
        
        val=maxDiameter(root)
        return max(maxPath[0],val)

        



        
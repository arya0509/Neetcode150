# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if(not root):
            return 0
        
        return self.recursion(root,0)
    
    def recursion(self,root,val):
        if(not root):
            return val
        val+=1
        left=root.left
        right=root.right

        maxVal=max(self.recursion(left,val),self.recursion(right,val))

        return maxVal
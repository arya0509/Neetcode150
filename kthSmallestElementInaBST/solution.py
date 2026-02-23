# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        val=[]
        def findVal(root):
            if not root:
                return 
            
            findVal(root.left)
            val.append(root.val)
            findVal(root.right)
        findVal(root)
        return val[k-1]


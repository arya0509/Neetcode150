# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count=0
        def countGoodNodes(root,maxVal):
            if not root:
                return 
            if(root.val>=maxVal):
                self.count+=1
            else:
                maxVal=root.val
            countGoodNodes(root.left,maxVal)
            countGoodNodes(root.right,maxVal)
        countGoodNodes(root,root.val)
        return self.count
            
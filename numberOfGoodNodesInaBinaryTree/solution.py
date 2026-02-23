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
        if not root:
            return 
        count=[1]
        max=root.val

        def recursion(max,root):
            if not root:
                return 
            
            if(root.val>=max):
                max=root.val
                count.append(1)
            
            recursion(max,root.left)
            recursion(max,root.right)
        
        recursion(max,root.left)
        recursion(max,root.right)
        return len(count)
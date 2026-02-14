# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
       
        
        
        
        maxSum=0
        def recursion(root):
            nonlocal maxSum
            if(not root):
                return 0
            
            left=root.left
            right=root.right
         
            leftLen=recursion(left)
            rightLen=recursion(right)

            maxSum=max(maxSum,leftLen+rightLen)
            
            return 1+max(leftLen,rightLen)
        recursion(root)
        return maxSum


node1 = TreeNode(1)
node2 = TreeNode(2)

node1.left = node2  


sol=Solution()
print(sol.diameterOfBinaryTree(node1))

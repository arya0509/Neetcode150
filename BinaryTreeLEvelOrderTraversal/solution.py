from collections import defaultdict 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        nodeDict=defaultdict(list)
        nodeDict[1]=[root.val]
        level=2
        def recursion(left,right,level):
            if(not right and not left):
                return 
            elif(not left):
                nodeDict[level].extend([right.val])  
                recursion(right.left,right.right,level+1)           
            elif(not right):
                nodeDict[level].extend([left.val])  
                recursion(left.left,left.right,level+1)   
            else:
                nodeDict[level].extend([left.val,right.val]) 
                level+=1
                recursion(left.left,left.right,level)
                recursion(right.left,right.right,level)
                
        recursion(root.left,root.right,level)
        nodeList=[]
        for level in range(1,len(nodeDict)+1):
            nodeList.append(nodeDict[level])
        
        return nodeList

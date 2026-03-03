# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res=[]
        def preOrder(root):
            if not root:
                self.res.append("N")
                return 
            self.res.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)

        self.res=",".join(self.res)
        return self.res
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        list=data.split(",")
        self.index=0
        def construct(root):
            if root=="N":
                self.index+=1
                return None
            node=TreeNode(int(list[self.index]))
            self.index+=1
            node.left=construct(list[self.index])
            node.right=construct(list[self.index])
            return node  
        return construct(list[0])
        
            

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
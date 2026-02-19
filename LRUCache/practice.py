class DoublyLinkedList(object):
    def __init__(self,key,val,prev=None,next=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next
                
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.left=DoublyLinkedList(0,0)
        self.right=DoublyLinkedList(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        self.LRUDict={}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if(key in self.LRUDict):
            self.remove(self.LRUDict[key])
            self.insert(self.LRUDict[key])
            return self.LRUDict[key].val
        return -1
       

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if(key in self.LRUDict):
            self.remove(self.LRUDict[key])
            self.LRUDict[key].val=value
            self.insert(self.LRUDict[key])
        else:
            self.LRUDict[key]=DoublyLinkedList(key,value)
            self.insert(self.LRUDict[key])
            if(len(self.LRUDict)>self.capacity):
                del self.LRUDict[self.left.next.key]

                self.remove(self.left.next)
        

    
    def remove(self,node):
        
       node.prev.next=node.next
       node.next.prev=node.prev
    
    def insert(self,node):
        prev=self.right.prev
        next=self.right

        prev.next=node
        node.next=next
        node.prev=prev

        next.prev=node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
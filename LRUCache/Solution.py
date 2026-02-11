class Node(object):
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.next=self.prev=None
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap=capacity
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next,self.right.prev=self.right,self.left
        self.hash={}
    def remove(self,n):
        prv,nxt=n.prev,n.next
        prv.next=nxt
        nxt.prev=prv

    def insert(self,n):
        prv,nxt=self.right.prev,self.right
        prv.next=n
        nxt.prev=n

        n.prev=prv
        n.next=nxt
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            self.remove(self.hash[key])
            self.insert(self.hash[key])
            return self.hash[key].val
        return -1

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if(key in self.hash):
            self.remove(self.hash[key])
        self.hash[key]=Node(key,value)
        self.insert(self.hash[key])
        
        if(len(self.hash)>self.cap):
            lru=self.left.next
            self.remove(lru)
            del self.hash[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
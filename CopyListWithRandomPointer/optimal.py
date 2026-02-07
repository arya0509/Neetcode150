from collections import defaultdict
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToNewDict=defaultdict(lambda:Node(0))
        oldToNewDict[None]=None

        curr=head
        while(head):
            oldToNewDict[curr].val=curr.val
            oldToNewDict[curr].next=oldToNewDict[curr.next]
            oldToNewDict[curr].random=oldToNewDict[curr.random]
            curr=curr.next
        
        return oldToNewDict[head]
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        nodeList=[]
        curr=head
        while(curr):
            nodeList.append(curr)
            curr=curr.next
        
        targetIndex=len(nodeList)-n
        if(nodeList[targetIndex-1]):
            nodeList[targetIndex-1].next=nodeList[targetIndex].next
            return head
        head=head.next
        return head

        
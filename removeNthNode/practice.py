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


        curr=head
        nodeList=[]
        while(curr):
            nodeList.append(curr)
            curr=curr.next

        target=len(nodeList)-n

        nodeList[target-1].next=nodeList[target].next

        return head
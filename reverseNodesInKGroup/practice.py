# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        temp=head
        count=1
        while(count<=k):
            if(temp==None):
                break
            temp=temp.next
            count+=1
            
        if(temp==None and count<=k):
                return head
        next=self.reverseKGroup(temp,k)

        curr=head
        count=1
        while(count<=k and curr):
            temp=curr.next
            curr.next=next

            next=curr
            curr=temp

            count+=1
        
        return next
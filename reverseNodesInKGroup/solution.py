# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        curr=head
        group=0
        while(curr and group<k):
            curr=curr.next
            group+=1
        
        if(k==group):
            curr=self.reverseKGroup(curr,k)
            while(group>0):
                temp=head.next
                head.next=curr

                curr=head
                head=temp

                group-=1
            head=curr
            
           
        return head


            

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=head
        fast=head
        pos=0
        while(fast):
            if(pos!=0 and slow ==fast):
                return True
            slow=slow.next
            fast=fast.next.next
            pos+=1
        
        return False
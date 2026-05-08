# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head.next
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        

        prev=None

        second=slow.next
        slow.next=None

        while(second):
            temp=second.next
            second.next=prev

            prev=second
            second=temp
        
        first=head
        second=prev

        while(second):
            
            first_next=first.next
            second_next=second.next

            first.next=second
            second.next=first_next

            first=first_next
            second=second_next
        
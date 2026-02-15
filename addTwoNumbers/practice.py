# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=curr=ListNode()
        carry=0
        while(l1 or l2):
            l1=ListNode() if not l1 else l1
            l2=ListNode() if not l2 else l2

            sum=l1.val + l2.val
            sum+=carry
            carry=0

            lastDigit=sum%10
            curr.next=ListNode(lastDigit)
            curr=curr.next
            
            carry=sum-lastDigit
            if(carry>9):
                carry=sum/10

            l1=l1.next
            l2=l2.next
        
        if(carry):
            curr.next=ListNode(carry)
        
        return dummy.next


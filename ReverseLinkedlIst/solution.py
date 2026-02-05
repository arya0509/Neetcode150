# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack=[]
        curr=head
        while(curr!=None):
            stack.append(curr.val)
            curr=curr.next
        newHead=ListNode()
        curr=newHead
        print(stack[::-1])
        for val in range(len(stack)-1,0,-1):
            if(curr==head):
                head.val=stack[val]
                curr.next=ListNode()
                curr=curr.next
                continue
           
            curr.val=stack[val]
            if(val+1!=len(stack)):
                curr.next=ListNode()
            curr=curr.next
       
        return newHead

    
sol=Solution()
print(sol.reverseList())

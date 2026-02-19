# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return []
        if (len(lists)==1):
            return lists[0]
        l=0
        r=len(lists)-1
        newList=[]
        while(l<r):
            head1=lists[l]
            head2=lists[r]

            newHead=self.sort(head1,head2)
            newList.append(newHead)
            l+=1
            r-=1
        if(l==r):
            newList.append(lists[l])
        
        return self.mergeKLists(newList)
    

    def sort(self,head1,head2):
        dummy=curr=ListNode()
        while(head1 and head2):
            if(head1.val<=head2.val):
                curr.next=head1
                curr=curr.next
                head1=head1.next
                
            else:
                curr.next=head2
                curr=curr.next
                head2=head2.next
        
        curr.next=head1 if not head2 else head2

        return dummy.next
                

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
        if(not lists):
            return lists
        if(len(lists)==1):
            return lists[0]
        l=0
        r=len(lists)-1
        newList=[]
        while(l<r):
            A=lists[l]
            B=lists[r]
            dummy=curr=ListNode()
            
            while(A and B):
                if(A.val<=B.val):
                    curr.next=A
                    curr,A=curr.next,A.next
                    continue
                curr.next=B
                curr,B=curr.next,B.next
            curr.next=A if(not B) else B
            newList.append(dummy.next)
            l+=1
            r-=1
        if(l==r):
            newList.append(lists[l])
        return self.mergeKLists(newList)
                
            
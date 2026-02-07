# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        listNodes=[]
        curr=head
        while(curr):
            listNodes.append(curr)
            curr=curr.next 
        l=0
        r=len(listNodes)-1
        while(l<=r):
            if(l==r):
                listNodes[r].next=None  
                break           
            if(l+1==r):               
                listNodes[r].next=None            
                break
            listNodes[l].next=listNodes[r]          
            listNodes[r].next=listNodes[l+1]
            l+=1
            r-=1
     



node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5





sol=Solution()

finalNode=(sol.reorderList(node1))
id=0
while(node1):
    # if(id==6):
    #     break
    print(node1.val,end=",")
    node1=node1.next
    id+=1
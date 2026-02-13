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
        nodeList=[]

        curr=head
        while(curr):
            nodeList.append(curr)
            curr=curr.next
        
        left=0
        right=len(nodeList)-1
        while(left<right):
            next=nodeList[left].next
            nodeList[left].next=nodeList[right]
            if(nodeList[right]!=next):
                nodeList[right].next=next
            else:
                nodeList[right].next=None
            left+=1
            right-=1
        if(left==right):
            nodeList[left].next=None
        
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
print("Ho")
finalNode=(sol.reorderList(node1))
id=0
while(node1):
    if(id==6):
        break
    print(node1.val,end=",")
    node1=node1.next
    id+=1
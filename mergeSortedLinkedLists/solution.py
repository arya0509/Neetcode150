# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=node=ListNode()

        while(list1 and list2):
            if(list1.val<=list2.val):
                node.next=list1
                list1=list1.next
            else:
                node.next=list2
                list2=list2.next
            node=node.next
        
        node.next=list1 or list2

        return temp.next

node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(4)

node1.next=node2
node2.next=node3


node4=ListNode(1)
node5=ListNode(3)
node6=ListNode(4)

node4.next=node5
node5.next=node6

sol=Solution()

finalNode=(sol.mergeTwoLists(node1,node4))

while(finalNode):
    print(finalNode.val,end=",")
    finalNode=finalNode.next
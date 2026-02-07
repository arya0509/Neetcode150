# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr=head
        if not head:
            return head
        nodeDict={}
        index=0
        while(curr):
            nodeDict[curr]=index
            index+=1
            curr=curr.next
        nodeList=[]
        for i in range(len(nodeDict)):
            nodeList.append(Node(0))

        for node in nodeDict:
            nodeList[nodeDict[node]].val=node.val 
            nextNode=nodeList[nodeDict[node.next]] if (node.next) else None
            random=nodeList[nodeDict[node.random]] if (node.random) else None
            
            nodeList[nodeDict[node]].next=nextNode
            nodeList[nodeDict[node]].random=random

            print(nodeList[nodeDict[node]].val,end=",")
            print(f"Index: {nodeDict[node]}")
           
       
        return nodeList[0]

node1=Node(7)
node2=Node(13)
node3=Node(11)
node4=Node(10)
node5=Node(1)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node2.random=node1
node3.random=node5
node4.random=node3
node5.random=node1





sol=Solution()
print(sol.copyRandomList(node1).val)
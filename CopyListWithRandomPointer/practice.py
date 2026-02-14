
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
        originalList=[]
        indexDict={}
        index=0
        curr=head
        while(curr):
            originalList.append(curr)
            indexDict[curr]=index
            index+=1
            curr=curr.next
           
        indexDict[None]=None
        newList=[]
        for i in range(len(originalList)):
            newList.append(Node(0))
        
        for i in range(len(newList)):
            newList[i].val=originalList[i].val

            nextIndex=indexDict[originalList[i].next]
            randomIndex=indexDict[originalList[i].random]
            if(nextIndex):
                newList[i].next=newList[nextIndex]
            if(randomIndex):
                newList[i].random=newList[randomIndex]
           
       
        return newList[0]

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
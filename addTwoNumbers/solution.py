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
        dummy=NodeList()
        curr=dummy
        remaining=0
        l1Curr=l1
        l2Curr=l2
        NodeList=[]
        
        while(l1Curr or l2Curr):

            val1=l1Curr.val if (l1Curr) else 0
            val2=l2Curr.val if (l2Curr) else 0
            sum=val1+val2
            sum+=remaining
            lastDigit=sum%10
           
                
            remaining=(sum-lastDigit)/10 
                    
            NodeList.append(ListNode(lastDigit))   
            curr.next= ListNode(lastDigit)     
            l1Curr=l1Curr.next if(l1Curr) else None 
            l2Curr=l2Curr.next if(l2Curr) else None
            curr=curr.next
        if(remaining):
            NodeList.append(ListNode(remaining))      
        head=NodeList[0]
     
        index=0
        while(index+1<len(NodeList)):
            NodeList[index].next=NodeList[index+1]
            index+=1
        
        return dummy.next
                

            


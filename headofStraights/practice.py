class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        hand.sort()
        exists={}
        for num in hand:
            exists[num]=exists.get(num,0)+1
        start=hand[0]
        end=hand[-1]
       
        while(end>start-1):
           
            if(end in exists and exists.get(end,0)!=0):
              
                for i in range(0,groupSize):
                    # print(end-i)
                    if(end-i not in exists  or exists.get(end-i,-1)==0):
                        return False
                    exists[end-i]-=1
                if(exists.get(end,0)==0):
                    end-=1
        return True 
                
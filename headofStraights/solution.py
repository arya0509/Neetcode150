from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if(len(hand)%groupSize!=0):
            return False
        count=Counter(hand)
        for num in hand:
            if(count[num]):
                for i in range(num,num+groupSize):
                    if(not count[i]):
                        return False
                    count[i]-=1
        return True
        
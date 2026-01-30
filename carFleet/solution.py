from operator import itemgetter
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        stack=[]
        sortedTimeAndPosition=[0] * len(position)

        for i in range(len(speed)):
            sortedTimeAndPosition[i]=[position[i],speed[i]]
        
        for p,s in sorted(sortedTimeAndPosition)[::-1]:
            stack.append((target-p)/s)
            if(len(stack)>=2 and stack[-1]>=stack[-2]):
                stack.pop()
        
        return len(stack)
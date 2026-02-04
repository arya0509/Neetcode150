class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        targetAndPosition=[]
        for i in range(len(position)):
            targetAndPosition.append([position[i],speed[i]])
        
        
       
        stack=[]

        for tp in sorted(targetAndPosition,reverse=True):
            time=(target-tp[0])/tp[1]
            print(time)
            if(stack and stack[-1]>=time):
                continue
            stack.append(time)
        
        return len(stack)
sol=Solution()
print(sol.carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))
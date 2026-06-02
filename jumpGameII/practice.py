class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        max=0
        count=0
        while(max<len(nums)-1):
            count+=1
            currMax=0

            while(i<max+1):
               
                if(nums[i]+i>currMax):
                    currMax=nums[i]+i
                i+=1
            max=currMax
        return count 
    
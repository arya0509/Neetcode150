class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps=0
        maxRange=0
        l=r=0
        while(r<len(nums)-1):
            steps+=1
            for i in range(l,r+1):
                maxRange=max(maxRange,i+nums[i])
            r=maxRange
            l+=1
        return steps 
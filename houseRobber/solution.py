class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums<=2)):
            return max(nums)
        one=1
        two=0
        maxSeq=[num for num in nums]
        maxSeq[2]=maxSeq[2]+maxSeq[1]
        self.res=0
        for i in range(3,len(nums)):
            temp=nums[i]+nums[one]
            temp1=nums[i]+nums[two]
            maxSeq[i]=max(temp1,temp)
            self.res=max(self.res,maxSeq[i])
            one+=1
            two+=1

        return self.res
            
        
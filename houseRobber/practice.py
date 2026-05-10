class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<=2):
            return max(nums)
        maxSeq=[num for num in nums]

        maxSeq[2]+=maxSeq[0]
        one=1
        two=0
        res=max(nums[one],nums[two])
        for i in range(3,len(nums)):
            oneSum=maxSeq[one]+maxSeq[i]
            twoSum=maxSeq[two]+maxSeq[i]

            maxSeq[i]=max(oneSum,twoSum)
            res=max(res,maxSeq[i])
        return res





        
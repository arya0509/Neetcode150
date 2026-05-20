class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=float("-inf")
        maxVal=1
        minVal=1
        for num in nums:
            temp=maxVal
            if(num<=0):
                maxVal=minVal*num
                minVal=min(temp*num,num)
            else:
                maxVal=max(temp*num,num)
                minVal=min(minVal*num,num)
            res=max(res,maxVal)
      
        return res

                


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.recursion(nums,[False]*len(nums),[],res)
        return res
    def recursion(self,nums,check,current,res):
        if(len(nums)==len(current)):
            res.append(current[:])
            return 
        for i in range(len(nums)):
            if(not check[i]):
                current.append(nums[i])
                check[i]=True
                self.recursion(nums,check,current,res)
                current.pop()
                check[i]=False

                
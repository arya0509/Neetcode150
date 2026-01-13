class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dictionary={}
        index=0
        for i in nums:
            if dictionary.get(i) !=None:
                return True
            dictionary[i]=index
            index=index+1
        return False

sol= Solution()
print(sol.containsDuplicate([1,2,3,1]))
        
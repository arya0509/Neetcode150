class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_set=set(nums)
        max_length=1 
        for num in nums_set:
            if(num-1) not in nums_set:
                length=1
                while(num+length in nums_set):
                    length+=1

                    if(max_length<length):
                        max_length=length

        return max_length
    

sol=Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))
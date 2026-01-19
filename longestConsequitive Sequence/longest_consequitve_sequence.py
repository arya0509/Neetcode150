class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        
        if(len(nums)<=1):
            return len(nums)
        left=0
        right=1
        max_len=1
        curr_len=1
        while(left!=right and right!=len(nums)):
           
           
            if(nums[left]+1==nums[right]):
                curr_len+=1
                if(max_len<=curr_len):
                    max_len=curr_len
            elif(nums[left]==nums[right]):
                right+=1
                left+=1
        
                continue

            else:
                curr_len=1
            right+=1
            left+=1
        
        return max_len


sol=Solution()
print(sol.longestConsecutive([1,0,1,2]))
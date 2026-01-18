from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count=defaultdict(int)
        freq_list=[[] for i in range(len(nums)+1)]

        for i in nums:
            
            count[i]=count[i]+1
               
        for num in count:
            freq_list[count[num]].append(num)

        output=[]
        for i in range(len(freq_list)-1,len(freq_list)-k,-1):
            for j in freq_list[i]:
                output.append(j)
                if(len(output)==k):
                    return output
        
        

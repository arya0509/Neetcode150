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
        print (len(freq_list)-k)
        output=[]
        for i in range(len(freq_list)-1,-1,-1):
            for j in freq_list[i]:
                output.append(j)
                if(len(output)==k):
                    return output
                    
sol=Solution()
print(sol.topKFrequent([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6],10))




        
        

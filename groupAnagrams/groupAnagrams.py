from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        
        """


        output=defaultdict(list)
        for i in strs:
            key="".join(sorted(i))
            output[key].append(i)
        return output.values()
    
       

sol= Solution()
print (sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        mergedList=nums1
       
        if len(mergedList)%2!=0:
            return sorted(mergedList)[len(mergedList)//2]
        
        sorted_list=sorted(mergedList)
        
        middleRight=len(sorted_list)/2
        middleLeft=middleRight-1
        averageElem= float(sorted_list[middleLeft]+sorted_list[middleRight])/2
        return averageElem
        
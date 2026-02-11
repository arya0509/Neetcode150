class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A,B=nums1,nums2
        
        if(len(nums2)<len(nums1)):
            A,B=B,A
        total=len(A)+len(B)
        half=total//2
        l=0
        r=len(A)-1
        while(True):
            i=(l+r)//2
            j=(half-2)-i

            ALeft=A[i] if(i>=0) else float("-infinity")
            ARight=A[i+1] if(i+1<len(A)) else float("infinity")
            BLeft=B[j] if(j>=0) else float("-infinity")
            BRight=B[j+1] if(j+1<len(B)) else float("infinity")

            if(ALeft<=BRight and BLeft<=ARight):
                if(total%2!=0):
                    return min(ARight,BRight)
                return float(max(ALeft,BLeft) +min(ARight,BRight))/2
            elif(ALeft>BRight):
                r=i-1
            else:
                l=i+1



